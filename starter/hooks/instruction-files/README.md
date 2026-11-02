# Schutz vor fremden Anweisungsdateien

Claude Code und Codex laden bestimmte Dateien automatisch als Anweisung. Liegt eine fremde Vorlage unter so einem Namen im Workspace, wirkt sie wie eine eigene Regel (Prompt-Injection, also eingeschleuste Anweisungen). Diese Hooks prüfen das technisch, statt sich auf eine Bitte in der `AGENTS.md` zu verlassen.

| Dateiname | Wer lädt ihn |
|---|---|
| `CLAUDE.md`, `CLAUDE.local.md` | Claude Code |
| `AGENTS.md`, `AGENTS.override.md` | Codex und andere Agenten |
| `SKILL.md` | Claude Code und Codex (Skills) |
| `GEMINI.md` | andere Agenten |

Die Hooks achten auf alle diese Namen, egal mit welchem Programm du arbeitest.

| Datei | Aufgabe |
|---|---|
| `scan.py` | beim Start einer Session: durchsucht den Workspace und den Skill-Ordner (`~/.claude/skills`, bei Codex `~/.agents/skills`) und meldet alles, was nicht auf der Liste steht |
| `guard.py` | vor jedem Schreiben: hält an, bevor eine solche Datei entsteht, ein neuer Skill-Ordner beschrieben wird oder Liste und Hooks geändert werden. Claude Code fragt dann nach, Codex lehnt ab |
| `common.py` | gemeinsame Teile: Dateinamen, übersprungene Ordner, Laden der Liste |
| `allowlist.example.txt` | Muster für `allowlist.txt`: erlaubte Dateien und Skill-Ordner, pflegt nur die Person selbst |
| `config.example.json` | Muster für `config.json`: Pfad des Workspace und Programm (`"agent": "claude"` oder `"codex"`) |

Voraussetzung: Python 3. Der Skill `setup` richtet alles in Schritt 6 ein. Die Beschreibung hier ist für die Einrichtung von Hand.

## Einrichten (Claude Code)

1. Ordner `~/.claude/hooks/instruction-files/` anlegen (Windows: `C:/Users/<name>/.claude/hooks/instruction-files/`) und `common.py`, `scan.py`, `guard.py` hineinkopieren.
2. `config.example.json` als `config.json` dorthin kopieren, den Pfad des Workspace eintragen, mit `/`, und `"agent": "claude"` lassen.
3. `allowlist.example.txt` als `allowlist.txt` dorthin kopieren. Sie gilt nur für Claude Code. Jede Zeile ist ein absoluter Pfad mit `/` oder `~`, zum Beispiel `/Users/anna/workspace/AGENTS.md`. Relative Pfade erkennt der Hook nicht, dann gilt jede Datei als fremd. Eintragen:
   - die Anweisungsdateien im Workspace: `<workspace>/AGENTS.md`, `<workspace>/CLAUDE.md`, `<workspace>/<Vault-Name>/AGENTS.md`, `<workspace>/<Vault-Name>/CLAUDE.md`
   - beide Kopien des Setup-Skills: `<workspace>/.claude/skills/setup/SKILL.md` und `<workspace>/.agents/skills/setup/SKILL.md`
   - `<workspace>/starter/skills/<name>/SKILL.md` für jeden Skill im Starter
   - `skill:<name>` für jeden Ordner in `~/.claude/skills/` (dort sucht Claude Code Skills)
4. In `~/.claude/settings.json` auf oberster Ebene ergänzen (bei vorhandenem `"hooks"` nur die beiden Einträge).

macOS und Linux:

```json
"hooks": {
  "SessionStart": [
    {
      "matcher": "startup|resume|clear|compact",
      "hooks": [
        { "type": "command", "command": "python3", "args": ["-I", "/Users/anna/.claude/hooks/instruction-files/scan.py"] }
      ]
    }
  ],
  "PreToolUse": [
    {
      "matcher": "Write|Edit|MultiEdit|NotebookEdit|Bash|PowerShell",
      "hooks": [
        { "type": "command", "command": "python3", "args": ["-I", "/Users/anna/.claude/hooks/instruction-files/guard.py"] }
      ]
    }
  ]
}
```

Windows: gleich, aber `"command": "py"` und als erstes Argument `"-3"`, also zum Beispiel `"args": ["-3", "-I", "C:/Users/anna/.claude/hooks/instruction-files/scan.py"]`.

Mit `args` startet Claude Code das Programm direkt, ohne Shell. Deshalb funktioniert es unter Windows auch ohne Git Bash.

## Codex

1. Ordner `~/.codex/hooks/instruction-files/` anlegen (Windows: `C:/Users/<name>/.codex/hooks/instruction-files/`) und `common.py`, `scan.py`, `guard.py` hineinkopieren.
2. `config.json` dort anlegen, mit dem Pfad des Workspace und dem Programm:

   ```json
   { "workspace": "/home/anna/workspace", "agent": "codex" }
   ```

3. Eine eigene `allowlist.txt` dort anlegen (Muster: `allowlist.example.txt`). Sie gilt nur für Codex. Jede Zeile ist ein absoluter Pfad mit `/` oder `~`, zum Beispiel `/home/anna/workspace/AGENTS.md`. Relative Pfade erkennt der Hook nicht, dann gilt jede Datei als fremd. Eintragen:
   - die Anweisungsdateien im Workspace: `<workspace>/AGENTS.md`, `<workspace>/CLAUDE.md`, `<workspace>/<Vault-Name>/AGENTS.md`, `<workspace>/<Vault-Name>/CLAUDE.md`
   - beide Kopien des Setup-Skills: `<workspace>/.claude/skills/setup/SKILL.md` und `<workspace>/.agents/skills/setup/SKILL.md`
   - `<workspace>/starter/skills/<name>/SKILL.md` für jeden Skill im Starter
   - `~/.codex/AGENTS.md`
   - `skill:<name>` für jeden Ordner in `~/.agents/skills/` (dort sucht Codex Skills)
4. In `~/.codex/config.toml` (die Einstellungen von Codex) die Hooks einschalten:

   ```toml
   [features]
   hooks = true
   ```

   Gibt es `[features]` schon, nur die Zeile `hooks = true` ergänzen. Ältere Codex-Versionen nennen den Schalter `codex_hooks`.
5. In `~/.codex/hooks.json` eintragen. Gibt es die Datei schon, nur die beiden Einträge unter `"hooks"` ergänzen:

```json
{
  "hooks": {
    "SessionStart": [
      { "matcher": "startup|resume|clear|compact",
        "hooks": [ { "type": "command",
          "command": "python3 -I \"/home/anna/.codex/hooks/instruction-files/scan.py\"",
          "commandWindows": "py -3 -I \"C:/Users/anna/.codex/hooks/instruction-files/scan.py\"" } ] }
    ],
    "PreToolUse": [
      { "matcher": "apply_patch|Write|Edit|Bash",
        "hooks": [ { "type": "command",
          "command": "python3 -I \"/home/anna/.codex/hooks/instruction-files/guard.py\"",
          "commandWindows": "py -3 -I \"C:/Users/anna/.codex/hooks/instruction-files/guard.py\"" } ] }
    ]
  }
}
```

`/home/anna` durch deinen Benutzerordner ersetzen (macOS: `/Users/<name>`). Codex kennt kein `args`: Der ganze Aufruf steht in einer Zeile in `command`, unter Windows in `commandWindows`. Deshalb stehen die Pfade in doppelten Anführungszeichen, sonst bricht ein Leerzeichen im Pfad den Aufruf.

Unterschiede zu Claude Code:

- **Ablehnen statt fragen:** Codex kennt bei diesen Hooks keine Rückfrage. Es lehnt das Schreiben ab und sagt in der Meldung, welche Zeile du in `allowlist.txt` eintragen musst. Danach noch einmal versuchen lassen.
- **Einmal bestätigen:** Codex lässt neue Hooks eventuell einmal bestätigen, bevor sie laufen (Trust). Das ist gewollt.
- **Neue Projekte:** Beim Anlegen eines Projekts unter `projects/` entstehen `AGENTS.md` und `CLAUDE.md`. Codex lehnt das zuerst ab. Trag die beiden absoluten Pfade selbst in `~/.codex/hooks/instruction-files/allowlist.txt` ein und lass es erneut versuchen.
- **Verbote sind lückenhaft:** Die Verbote in `~/.codex/rules/starter.rules` (kein Force-Push, kein rekursives Löschen) erkennen nur die übliche Schreibweise. `git push origin --force` (Option an anderer Stelle) und PowerShell `Remove-Item -Recurse` fallen durch. Ein Leseverbot für `.env`-Dateien kennt Codex nicht, das steht nur als Regel in der `AGENTS.md`.

## Testen

1. Neue Session: Es darf keine Warnung kommen.
2. „Leg im Workspace eine Datei `test/CLAUDE.md` an“: Claude Code muss nachfragen (ablehnen), Codex muss ablehnen.
3. Eine Datei `CLAUDE.md` von Hand in einen Ordner im Vault legen, neue Session: Es muss eine Warnung kommen. Danach die Datei löschen.

Die Skripte lassen sich über Umgebungsvariablen gegen einen Testordner laufen: `INSTRUCTION_ALLOWLIST`, `INSTRUCTION_WORKSPACE`, `INSTRUCTION_SKILLS_DIR`, `INSTRUCTION_AGENT` (`claude` oder `codex`).

## Grenzen

- Entpacken oder Klonen vieler Dateien fällt erst beim nächsten Start einer Session auf, wenn der Befehl keinen der Namen enthält.
- Gegen Prompt-Injection in normalen Texten (Webseiten, PDFs, Ausgaben von Programmen) helfen die Hooks nicht.
- Ein Fehler in `scan.py` blockiert die Session nicht, ein Fehler in `guard.py` führt zur Rückfrage (Codex: zur Ablehnung).
