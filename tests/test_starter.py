"""Tests für den Aufbau des Starters."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAMES = {"claude.md", "claude.local.md", "agents.md", "agents.override.md", "skill.md", "gemini.md"}
# Nur diese Dateien dürfen Claude als Anweisung dienen, wenn jemand den Starter öffnet
EXPECTED_INSTRUCTION_FILES = {
    "AGENTS.md",
    "CLAUDE.md",
    ".claude/skills/setup/SKILL.md",
    ".agents/skills/setup/SKILL.md",
}


def test_only_expected_instruction_files():
    found = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file() and p.name.lower() in NAMES and ".git" not in p.parts
    }
    # Skills unter starter/skills/ werden installiert, nicht geladen
    found = {f for f in found if not f.startswith("starter/skills/")}
    assert found == EXPECTED_INSTRUCTION_FILES


def test_bootstrap_marker_and_state():
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert text.startswith("<!-- starter:bootstrap v1 -->")
    assert "Einrichtung: offen" in text


def test_json_templates_are_valid():
    for path in (ROOT / "starter").rglob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))


def test_templates_referenced_by_setup_exist():
    skill = (ROOT / ".claude" / "skills" / "setup" / "SKILL.md").read_text(encoding="utf-8")
    for name in ("root-AGENTS.template.md", "vault-AGENTS.template.md", "vault-CLAUDE.template.md",
                 "programmieren.template.md", "projects-README.template.md", "STAND.template.md",
                 "settings-fragment.json", "starter.example.json", "codex-global-AGENTS.template.md",
                 "codex-config-fragment.toml", "codex-starter.rules"):
        assert name in skill
        assert (ROOT / "starter" / "templates" / name).is_file()


def test_setup_copies_are_identical():
    for name in ("SKILL.md", "fragen.md"):
        a = (ROOT / ".claude/skills/setup" / name).read_bytes()
        b = (ROOT / ".agents/skills/setup" / name).read_bytes()
        assert a == b, name


def test_setup_covers_both_agents():
    text = (ROOT / ".claude/skills/setup/SKILL.md").read_text(encoding="utf-8")
    for required in ("~/.codex/config.toml", "~/.agents/skills/", "~/.claude/settings.json", "10-Arbeit/",
                     "starter-ausgabe/", "{{SEAL}}", "{{AGENT_NAME}}", "apply_patch", "Nur Claude Code:",
                     "Nur Codex:"):
        assert required in text, required


def test_setup_questions_use_arbeit_folder():
    text = (ROOT / ".claude/skills/setup/fragen.md").read_text(encoding="utf-8")
    assert "10-Arbeit/" in text and "Aktualisierung" in text
    assert "mit Claude Code" not in text


def test_bootstrap_is_neutral():
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "Claude Code oder Codex" in text


def test_vault_rules_template_renamed():
    assert (ROOT / "starter/templates/vault-AGENTS.template.md").is_file()
    assert (ROOT / "starter/templates/vault-CLAUDE.template.md").read_text(encoding="utf-8").strip() == "@AGENTS.md"


def test_vault_template_uses_arbeit_folder():
    text = (ROOT / "starter/templates/vault-AGENTS.template.md").read_text(encoding="utf-8")
    assert "{{BEREICHE_ZEILEN}}" in text and "AGENTS.md" in text


def test_root_template_mentions_stand_and_neutral_seal():
    text = (ROOT / "starter/templates/root-AGENTS.template.md").read_text(encoding="utf-8")
    assert "STAND.md" in text and "{{SEAL}}" in text and "/seal-session" not in text


def test_templates_have_markers():
    for name in ("root-AGENTS.template.md", "vault-AGENTS.template.md", "codex-global-AGENTS.template.md"):
        text = (ROOT / "starter/templates" / name).read_text(encoding="utf-8")
        assert text.startswith("<!-- starter:begin v1 -->") and text.rstrip().endswith("<!-- starter:end v1 -->")


def test_codex_toml_template_is_valid():
    import tomllib
    data = tomllib.loads((ROOT / "starter/templates/codex-config-fragment.toml").read_text(encoding="utf-8"))
    assert data["sandbox_workspace_write"]["writable_roots"] == ["{{WORKSPACE}}"]


def test_codex_rules_forbid_force_push_and_rm_rf():
    text = (ROOT / "starter/templates/codex-starter.rules").read_text(encoding="utf-8")
    assert text.count("prefix_rule(") == 3
    assert text.count('decision = "forbidden"') == 3
    assert '"--force"' in text and '"-rf"' in text


def test_seal_session_skill_is_generic():
    text = (ROOT / "starter/skills/seal-session/SKILL.md").read_text(encoding="utf-8")
    assert text.startswith("---\nname: seal-session\n")
    for forbidden in ("Silver", "C:\\", "C:/Users/", "10-daten", "20-rezepte"):
        assert forbidden not in text
    for required in ("10-Arbeit/", "STAND.md", "40-Fehlerbaum/Eintraege/", "30-Sessions/", "$seal-session"):
        assert required in text


def test_handouts_cover_codex_and_mint():
    checklist = (ROOT / "starter/handout/Vorab-Checkliste.md").read_text(encoding="utf-8")
    trouble = (ROOT / "starter/handout/Troubleshooting.md").read_text(encoding="utf-8")
    hooks = (ROOT / "starter/hooks/instruction-files/README.md").read_text(encoding="utf-8")
    assert "codex --version" in checklist and ".deb" in checklist
    assert "libfuse2" in trouble and "starter-ausgabe" in trouble
    assert "hooks.json" in hooks and "commandWindows" in hooks


def test_vault_templates_do_not_name_one_program():
    vault = ROOT / "starter/templates/vault"
    assert (vault / "20-Konzepte/Beispiel - Gute Aufträge an deinen KI-Assistenten.md").is_file()
    for path in vault.rglob("*.md"):
        assert "Claude" not in path.read_text(encoding="utf-8"), path.name
        assert "Claude" not in path.name


def test_fehlerbaum_example_has_faelle_section():
    text = (ROOT / "starter/templates/vault/40-Fehlerbaum/Eintraege/Beispiel - Workspace in OneDrive.md")
    assert "## Fälle" in text.read_text(encoding="utf-8")


def test_codex_global_rules_only_apply_inside_workspace():
    text = (ROOT / "starter/templates/codex-global-AGENTS.template.md").read_text(encoding="utf-8")
    assert "außerhalb von `{{WORKSPACE}}`" in text


def test_internal_docs_are_not_exported():
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    for line in ("/docs export-ignore", "/tests export-ignore", "/.github export-ignore"):
        assert line in attributes
    assert not list((ROOT / "starter/docs").glob("2026-*"))
