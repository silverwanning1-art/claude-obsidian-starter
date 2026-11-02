"""Gemeinsame Teile der Hooks für Anweisungsdateien (CLAUDE.md, AGENTS.md, SKILL.md ...) für Claude Code und Codex."""
import json
import os
import unicodedata
from pathlib import Path

HOME = Path.home()
HERE = Path(__file__).resolve().parent
CONFIG = HERE / "config.json"


def _config(key):
    if CONFIG.is_file():
        return json.loads(CONFIG.read_text(encoding="utf-8")).get(key)
    return None


def _workspace():
    # Reihenfolge: Umgebungsvariable (für Tests), config.json (vom Skill setup), ~/workspace
    if os.environ.get("INSTRUCTION_WORKSPACE"):
        return Path(os.environ["INSTRUCTION_WORKSPACE"])
    value = _config("workspace")
    if value:
        return Path(os.path.expanduser(value))
    return HOME / "workspace"


def _agent():
    # Reihenfolge: Umgebungsvariable, config.json, sonst "claude"
    value = os.environ.get("INSTRUCTION_AGENT") or _config("agent") or "claude"
    return "codex" if str(value).strip().lower() == "codex" else "claude"


ALLOWLIST = Path(os.environ.get("INSTRUCTION_ALLOWLIST", HERE / "allowlist.txt"))
WORKSPACE = _workspace()
AGENT = _agent()
# Skill-Ordner: Claude Code liest ~/.claude/skills, Codex ~/.agents/skills
SKILLS_DIR = Path(os.environ.get(
    "INSTRUCTION_SKILLS_DIR",
    HOME / (".claude" if AGENT == "claude" else ".agents") / "skills"))
# Geschützt sind immer beide Programme, egal welches gerade läuft
HOOK_DIRS = [HERE, HOME / ".claude" / "hooks" / "instruction-files", HOME / ".codex" / "hooks" / "instruction-files"]
SKILL_DIRS = [SKILLS_DIR, HOME / ".claude" / "skills", HOME / ".agents" / "skills"]

# Dateinamen, die Claude Code, Codex oder andere Agenten als Anweisung laden
NAMES = {"claude.md", "claude.local.md", "agents.md", "agents.override.md", "skill.md", "gemini.md"}
# Ordner, die nicht durchsucht werden (Abhängigkeiten, Caches, generierte Daten)
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", ".uvcache", "__pycache__",
             ".pytest_cache", ".ruff_cache", ".mypy_cache", "dist", ".obsidian", ".trash"}


def norm(path) -> str:
    # NFC, sonst gelten gleich aussehende Pfade mit Umlauten als verschieden.
    # normcase: unter Windows Kleinbuchstaben und Backslashes, sonst unverändert.
    return os.path.normcase(unicodedata.normalize("NFC", os.path.abspath(os.path.expanduser(str(path)))))


def skill_name(name) -> str:
    return os.path.normcase(unicodedata.normalize("NFC", name))


def load_allowlist():
    """Liefert (erlaubte Dateipfade, erlaubte Skill-Ordner) oder None, wenn die Liste fehlt."""
    if not ALLOWLIST.is_file():
        return None
    paths, skills = set(), set()
    for line in ALLOWLIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("skill:"):
            skills.add(skill_name(line[len("skill:"):].strip()))
        else:
            paths.add(norm(line))
    return paths, skills
