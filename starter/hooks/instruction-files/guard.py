"""PreToolUse-Hook: fragt nach (Claude Code) bzw. blockiert (Codex), wenn eine Anweisungsdatei angelegt oder die Liste selbst geändert wird."""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import AGENT, ALLOWLIST, HOOK_DIRS, NAMES, SKILL_DIRS, load_allowlist, norm, skill_name  # noqa: E402

NAME_RE = re.compile(r"\b(claude|claude\.local|agents|agents\.override|skill|gemini)\.md\b", re.IGNORECASE)
# Befehle, die Dateien anlegen, kopieren, verschieben oder herunterladen (Bash und PowerShell)
WRITE_RE = re.compile(r">|\b(cp|mv|ln|curl|wget|tee|rsync|install|unzip|tar|ditto|touch)\b"
                      r"|\bgit\s+clone\b|\bsed\s+-i\b"
                      r"|\b(copy-item|move-item|rename-item|new-item|set-content|add-content|out-file"
                      r"|invoke-webrequest|iwr|expand-archive|copy|move|ren|ni|sc|ac)\b", re.IGNORECASE)
# Umleitungen, die keine Datei anlegen: 2>/dev/null, >&2, 2>&1, > $null
HARMLESS_REDIRECT_RE = re.compile(r"\d*>>?\s*(/dev/null|\$null)\b|\d*>&\s*\d+", re.IGNORECASE)
# Pfade in Befehlen mit / oder \ schreiben
GUARDED_CMD_RE = re.compile(r"\.claude[/\\]skills|\.agents[/\\]skills|hooks[/\\]instruction-files", re.IGNORECASE)
GUARDED_HOOK_DIRS = sorted({norm(d) for d in HOOK_DIRS})
GUARDED_SKILL_DIRS = sorted({norm(d) for d in SKILL_DIRS})
PATCH_MARKER = "*** Begin Patch"


def block(reason):
    # Codex kennt kein "ask", nur "deny" mit Begründung
    if AGENT == "codex":
        decision = "deny"
        reason += f" Wenn du die Datei bewusst willst: Pfad in {ALLOWLIST} eintragen und erneut versuchen."
    else:
        decision = "ask"
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason,
        }
    }, ensure_ascii=False))
    sys.exit(0)


def patch_paths(patch, cwd):
    """Absolute Pfade, die ein apply_patch anlegt, ändert oder verschiebt (Löschen wird ignoriert)."""
    paths = []
    for line in patch.splitlines():
        line = line.strip()
        for prefix in ("*** Add File: ", "*** Update File: ", "*** Move to: "):
            if line.startswith(prefix):
                path = os.path.expanduser(line[len(prefix):].strip())
                paths.append(path if os.path.isabs(path) else os.path.join(cwd, path))
    return paths


def check_file(path, allowed_paths, allowed_skills):
    path = norm(path)
    for folder in GUARDED_HOOK_DIRS:
        if path.startswith(folder + os.sep):
            block(f"Änderung an der Liste oder den Hooks für Anweisungsdateien: {path}")
    for folder in GUARDED_SKILL_DIRS:
        if path.startswith(folder + os.sep):
            skill = path[len(folder) + 1:].split(os.sep)[0]
            if skill_name(skill) not in allowed_skills:
                block(f"Neuer Skill-Ordner, der nicht auf der Liste steht: {skill}")
            return
    if os.path.basename(path).lower() in NAMES and path not in allowed_paths:
        block(f"Anweisungsdatei, die nicht auf der Liste steht: {path}. "
            "Fremde Vorlagen umbenennen, eigene in allowlist.txt eintragen.")


def check_command(cmd):
    if not WRITE_RE.search(HARMLESS_REDIRECT_RE.sub(" ", cmd)):
        return
    if NAME_RE.search(cmd):
        block("Der Befehl legt möglicherweise eine Anweisungsdatei (CLAUDE.md, AGENTS.md, SKILL.md ...) an.")
    if GUARDED_CMD_RE.search(cmd):
        block("Der Befehl ändert möglicherweise Skills oder die Hooks für Anweisungsdateien.")


def strings(value):
    """Alle Texte in tool_input, egal unter welchem Schlüssel (command, input, patch ...)."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        value = list(value.values())
    if isinstance(value, list):
        return [text for item in value for text in strings(item)]
    return []


def main():
    data = json.load(sys.stdin)
    tool = data.get("tool_name", "")
    tool_input = data.get("tool_input", {}) or {}
    cwd = data.get("cwd") or os.getcwd()
    allowlist = load_allowlist()
    if allowlist is None:  # Liste fehlt: nichts gilt als erlaubt
        allowlist = (set(), set())
    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
        if path:
            if not os.path.isabs(os.path.expanduser(path)):
                path = os.path.join(cwd, path)
            check_file(path, *allowlist)
    elif tool == "apply_patch":
        for path in patch_paths("\n".join(strings(tool_input)), cwd):
            check_file(path, *allowlist)
    elif tool in ("Bash", "PowerShell"):
        cmd = tool_input.get("command", "")
        if isinstance(cmd, list):
            cmd = "\n".join(str(part) for part in cmd)
        # apply_patch über die Shell (Heredoc oder Befehlsliste) wie einen Patch prüfen
        if PATCH_MARKER in cmd:
            for path in patch_paths(cmd, cwd):
                check_file(path, *allowlist)
        check_command(cmd)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # im Zweifel nachfragen statt durchlassen
        block(f"Prüfung der Anweisungsdateien fehlgeschlagen: {exc}")
