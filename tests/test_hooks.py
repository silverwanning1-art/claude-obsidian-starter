"""Tests für die Hooks gegen fremde Anweisungsdateien, laufen auf Windows, macOS und Linux."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

HOOKS = Path(__file__).resolve().parent.parent / "starter" / "hooks" / "instruction-files"


@pytest.fixture
def env(tmp_path):
    workspace = tmp_path / "workspace"
    skills = tmp_path / "skills"
    (workspace / "Wissen").mkdir(parents=True)
    (skills / "seal-session").mkdir(parents=True)
    (workspace / "AGENTS.md").write_text("eigene Regeln", encoding="utf-8")
    allowlist = tmp_path / "allowlist.txt"
    allowlist.write_text(
        f"{(workspace / 'AGENTS.md').as_posix()}\nskill:seal-session\n", encoding="utf-8"
    )
    return {
        **os.environ,
        "INSTRUCTION_WORKSPACE": str(workspace),
        "INSTRUCTION_SKILLS_DIR": str(skills),
        "INSTRUCTION_ALLOWLIST": str(allowlist),
    }, workspace, skills


def run(script, env, payload=None):
    result = subprocess.run(
        [sys.executable, "-I", str(HOOKS / script)],
        input=json.dumps(payload) if payload is not None else "",
        capture_output=True, text=True, encoding="utf-8", env=env, check=True,
    )
    return json.loads(result.stdout) if result.stdout.strip() else None


def decision(output):
    return output and output["hookSpecificOutput"]["permissionDecision"]


def test_scan_quiet_when_everything_is_listed(env):
    assert run("scan.py", env[0]) is None


def test_scan_reports_foreign_file_and_skill(env):
    environ, workspace, skills = env
    (workspace / "Wissen" / "CLAUDE.md").write_text("fremd", encoding="utf-8")
    (skills / "fremder-skill").mkdir()
    message = run("scan.py", environ)["systemMessage"]
    assert "claude.md" in message.lower()  # Windows zeigt Pfade kleingeschrieben (normcase)
    assert "fremder-skill" in message


def test_scan_matches_listed_path_regardless_of_case_on_windows(env):
    environ, workspace, _ = env
    if os.name != "nt":
        pytest.skip("nur unter Windows sind Pfade unabhängig von Groß- und Kleinschreibung")
    environ["INSTRUCTION_WORKSPACE"] = str(workspace).upper()
    assert run("scan.py", environ) is None


def test_guard_asks_for_new_instruction_file(env):
    environ, workspace, _ = env
    payload = {"tool_name": "Write", "tool_input": {"file_path": str(workspace / "x" / "CLAUDE.md")}}
    assert decision(run("guard.py", environ, payload)) == "ask"


def test_guard_allows_listed_file_and_normal_notes(env):
    environ, workspace, _ = env
    for name in ("AGENTS.md", "Notiz.md"):
        payload = {"tool_name": "Edit", "tool_input": {"file_path": str(workspace / name)}}
        assert run("guard.py", environ, payload) is None


@pytest.mark.parametrize("tool,command", [
    ("Bash", "cp vorlage.md ~/workspace/CLAUDE.md"),
    ("PowerShell", "Copy-Item vorlage.md C:\\Users\\anna\\workspace\\CLAUDE.md"),
    ("PowerShell", "Set-Content -Path C:\\Users\\anna\\.claude\\skills\\x\\notiz.md -Value x"),
])
def test_guard_asks_for_shell_commands(env, tool, command):
    payload = {"tool_name": tool, "tool_input": {"command": command}}
    assert decision(run("guard.py", env[0], payload)) == "ask"


@pytest.mark.parametrize("tool,command", [
    ("Bash", "cat CLAUDE.md 2>/dev/null"),
    ("PowerShell", "Get-Content CLAUDE.md"),
    ("PowerShell", "git status > $null"),
])
def test_guard_ignores_reading_commands(env, tool, command):
    payload = {"tool_name": tool, "tool_input": {"command": command}}
    assert run("guard.py", env[0], payload) is None


def codex(environ):
    return {**environ, "INSTRUCTION_AGENT": "codex"}


def patch_payload(workspace, body):
    patch = f"*** Begin Patch\n{body}*** End Patch\n"
    return {"tool_name": "apply_patch", "cwd": str(workspace), "tool_input": {"command": patch}}


def test_guard_denies_under_codex(env):
    environ, workspace, _ = env
    payload = {"tool_name": "Write", "tool_input": {"file_path": str(workspace / "x" / "CLAUDE.md")}}
    out = run("guard.py", codex(environ), payload)
    assert decision(out) == "deny"
    assert "allowlist" in out["hookSpecificOutput"]["permissionDecisionReason"]


def test_guard_checks_apply_patch_paths(env):
    environ, workspace, _ = env
    body = "*** Add File: notes/a.md\n+x\n*** Add File: vendor/AGENTS.md\n+y\n"
    assert decision(run("guard.py", codex(environ), patch_payload(workspace, body))) == "deny"


def test_guard_allows_apply_patch_on_normal_notes(env):
    environ, workspace, _ = env
    body = "*** Update File: Wissen/Notiz.md\n@@\n-a\n+b\n"
    assert run("guard.py", codex(environ), patch_payload(workspace, body)) is None


def test_guard_checks_move_to_in_patch(env):
    environ, workspace, _ = env
    body = "*** Update File: a.md\n*** Move to: x/SKILL.md\n@@\n-a\n+b\n"
    assert decision(run("guard.py", codex(environ), patch_payload(workspace, body))) == "deny"


def test_guard_handles_command_as_list(env):
    payload = {"tool_name": "Bash",
               "tool_input": {"command": ["bash", "-lc", "cp ~/Downloads/x.md ./CLAUDE.md"]}}
    assert decision(run("guard.py", env[0], payload)) == "ask"


def test_guard_protects_agents_skills_dir(env):
    payload = {"tool_name": "Bash", "tool_input": {"command": "cp -r foo ~/.agents/skills/foo"}}
    assert decision(run("guard.py", env[0], payload)) == "ask"


def test_scan_reports_agents_override(env):
    environ, workspace, _ = env
    (workspace / "AGENTS.override.md").write_text("fremd", encoding="utf-8")
    assert "agents.override.md" in run("scan.py", environ)["systemMessage"].lower()


def test_skills_dir_follows_agent():
    environ = {k: v for k, v in os.environ.items() if k != "INSTRUCTION_SKILLS_DIR"}
    environ["INSTRUCTION_AGENT"] = "codex"
    result = subprocess.run(
        [sys.executable, "-I", "-c", "import sys; sys.path.insert(0, sys.argv[1]); "
         "import common; print(common.SKILLS_DIR)", str(HOOKS)],
        capture_output=True, text=True, encoding="utf-8", env=environ, check=True,
    )
    assert result.stdout.strip().endswith(os.path.join(".agents", "skills"))


def test_guard_checks_patch_inside_shell_heredoc(env):
    environ, workspace, _ = env
    cmd = "apply_patch <<'EOF'\n*** Begin Patch\n*** Add File: x/AGENTS.md\n+fremd\n*** End Patch\nEOF\n"
    payload = {"tool_name": "Bash", "cwd": str(workspace), "tool_input": {"command": cmd}}
    assert decision(run("guard.py", codex(environ), payload)) == "deny"


def test_guard_checks_patch_as_command_list(env):
    environ, workspace, _ = env
    patch = "*** Begin Patch\n*** Add File: x/SKILL.md\n+fremd\n*** End Patch\n"
    payload = {"tool_name": "Bash", "cwd": str(workspace), "tool_input": {"command": ["apply_patch", patch]}}
    assert decision(run("guard.py", codex(environ), payload)) == "deny"


def test_guard_reads_patch_from_any_input_key(env):
    environ, workspace, _ = env
    patch = "*** Begin Patch\n*** Add File: x/AGENTS.md\n+fremd\n*** End Patch\n"
    payload = {"tool_name": "apply_patch", "cwd": str(workspace), "tool_input": {"input": patch}}
    assert decision(run("guard.py", codex(environ), payload)) == "deny"


def common_value(environ, name):
    result = subprocess.run(
        [sys.executable, "-I", "-c", "import sys; sys.path.insert(0, sys.argv[1]); "
         f"import common; print(common.{name})", str(HOOKS)],
        capture_output=True, text=True, encoding="utf-8", env=environ, check=True,
    )
    return result.stdout.strip()


def test_agent_value_is_normalized():
    environ = {**os.environ, "INSTRUCTION_AGENT": "Codex "}
    assert common_value(environ, "AGENT") == "codex"


@pytest.mark.parametrize("agent", ["claude", "codex"])
@pytest.mark.parametrize("target", [
    (".claude", "hooks", "instruction-files", "allowlist.txt"),
    (".codex", "hooks", "instruction-files", "allowlist.txt"),
    (".claude", "skills", "fremd", "notiz.md"),
    (".agents", "skills", "fremd", "notiz.md"),
])
def test_guard_protects_both_programs_regardless_of_agent(env, tmp_path, agent, target):
    environ, _, _ = env
    home = tmp_path / "home"
    environ = {**environ, "HOME": str(home), "USERPROFILE": str(home), "INSTRUCTION_AGENT": agent}
    payload = {"tool_name": "Write", "tool_input": {"file_path": str(home.joinpath(*target))}}
    assert decision(run("guard.py", environ, payload)) in ("ask", "deny")


def run_bytes(script, env, stdin=b""):
    """Wie ein Agent: Bytes rein und raus, unabhängig von der Codepage des Systems."""
    result = subprocess.run(
        [sys.executable, "-I", str(HOOKS / script)],
        input=stdin, capture_output=True, env=env, check=True,
    )
    return result.stdout


def test_guard_reads_utf8_and_answers_in_ascii(env):
    environ, workspace, _ = env
    path = workspace / "Über" / "CLAUDE.md"
    payload = {"tool_name": "Write", "tool_input": {"file_path": str(path)}}
    raw = run_bytes("guard.py", environ, json.dumps(payload, ensure_ascii=False).encode("utf-8"))
    assert raw.isascii()
    output = json.loads(raw)
    assert decision(output) == "ask"
    assert "über" in output["hookSpecificOutput"]["permissionDecisionReason"].lower()


def test_scan_answers_in_ascii(env):
    environ, workspace, _ = env
    folder = workspace / "Büro"
    folder.mkdir()
    (folder / "CLAUDE.md").write_text("x", encoding="utf-8")
    raw = run_bytes("scan.py", environ)
    assert raw.isascii()
    assert "büro" in json.loads(raw)["systemMessage"].lower()
