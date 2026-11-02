# Probelauf

Vor dem Workshop auf jedem System einmal komplett durchspielen, mit einem frischen Ordner und, wenn möglich, einem frischen Benutzerkonto ohne eigene `~/.claude/settings.json`.

| System | Wer | Stand |
|---|---|---|
| Windows mit Claude Code, Firmen-Laptop ohne Admin-Rechte | Autor | offen. Vorab bekannt: Git nur mit vollem Pfad, Python nur über `py` |
| macOS mit Claude Code | Autor | offen |
| Linux Mint mit Codex | Tester | offen |
| Windows mit Codex | – | ungetestet |
| macOS mit Codex | – | ungetestet |

## Ablauf

1. Vorab-Checkliste abarbeiten, Zeit notieren.
2. ZIP entpacken, Claude Code bzw. Codex im Ordner starten, „los“ schreiben.
3. Bei jedem Schritt die Uhrzeit notieren: Vorprüfung, Interview, Plan, Erzeugen, Einstellungen, Hooks, Kontext, Prüfung.
4. Neue Session: Kennt Claude Code bzw. Codex Name, Vault und Regeln? Kommt keine Warnung der Hooks?
5. Den Vault in Obsidian öffnen: Ordner, Vorlagen, Anhänge-Ordner richtig?
6. Einrichtung ein zweites Mal starten: Wird nur ergänzt, nichts überschrieben?

## Zu prüfen

- Claude Code, Obsidian, Git und Python ohne Admin-Rechte installierbar (Windows)
- Pfadangaben mit `/` in `additionalDirectories` unter Windows
- Die `deny`-Regel `PowerShell(Remove-Item * -Recurse *)` greift
- Hooks über `py -3` unter Windows
- Gesamtdauer gegen die geplanten 1,5 Stunden

## Linux Mint mit Codex: gezielt prüfen

Vorher `codex --version` notieren und `~/.codex/config.toml` sichern (`cp ~/.codex/config.toml ~/config.toml.bak`, falls sie existiert). Pro Punkt kurz festhalten, was du gesehen hast, auch bei „ok“.

Offene Fragen aus dem Entwurf sind mit (?) markiert. Dort sind wir auf deine Beobachtung angewiesen.

- [ ] Setup-Skill: Im entpackten Ordner (ohne `.git`) `codex` starten und `$setup` oder „los“ schreiben. Wird `.agents/skills/setup/` gefunden und die Einrichtung startet? (?)
- [ ] Schreibrechte außerhalb des Workspace: Codex schreibt nach `~/.codex/` und `~/.agents/skills/`. Wie oft fragt es, und kommst du durch? Bei Ablehnung: liegen die Dateien unter `starter-ausgabe/`, mit Zielpfad und Kopierbefehl (`mkdir -p`, `cp`), und stimmt der Befehl?
- [ ] `config.toml`: Nach der Einrichtung `diff ~/config.toml.bak ~/.codex/config.toml`. Nur ergänzt, bestehende Zeilen und Kommentare unverändert, neue Tabellen am Ende, keine doppelte Tabelle? Gültig als TOML (`python3 -c "import tomllib,sys; tomllib.load(open(sys.argv[1],'rb'))" ~/.codex/config.toml`)? `sandbox_mode` und `approval_policy` unverändert?
- [ ] `~/.codex/rules/starter.rules`: `codex execpolicy check --rules ~/.codex/rules/starter.rules git push --force origin main` meldet `forbidden` (Befehl an die aktuelle CLI anpassen, falls die Syntax abweicht). Auch `rm -rf build` prüfen und `git push origin main` (darf nicht verboten sein). Verbietet Codex wirklich, statt nachzufragen?
- [ ] Hooks einschalten: Ist `[features] hooks = true` nötig, oder lief es auch ohne? Heißt der Schalter in deiner Version `codex_hooks`? (?)
- [ ] Hooks bestätigen: Fragt Codex beim ersten Start nach einer Bestätigung (Trust-Abfrage) für `~/.codex/hooks.json`? (?)
- [ ] Warnung beim Start: Lege im Vault eine fremde Datei `CLAUDE.md` in einem Unterordner an, die nicht in `~/.codex/hooks/instruction-files/allowlist.txt` steht, und starte eine neue Session. Erscheint die Warnung „Unbekannte Anweisungsdateien“ und nennt sie die Datei?
- [ ] Schutz beim Schreiben: Bitte Codex, eine Datei `test/AGENTS.md` anzulegen (läuft über `apply_patch`). Wird sie abgelehnt, und ist die Begründung für Nichtprogrammierer verständlich? Fehlt die Datei danach (`ls test/`)?
- [ ] Was Codex an die Hooks schickt (einmal festhalten, der Schutz hängt davon ab): `~/codex-hook-debug.py` mit dem Inhalt `import pathlib, sys; f = pathlib.Path.home() / "codex-hook-stdin.jsonl"; f.open("a", encoding="utf-8").write(sys.stdin.read() + "\n")` anlegen und in `~/.codex/hooks.json` vorübergehend als zweiten Eintrag unter `PreToolUse` mit `"matcher": "apply_patch|Bash"` und `"command": "python3 -I \"/home/<name>/codex-hook-debug.py\""` ergänzen. Dann Codex eine normale Notiz anlegen lassen (`apply_patch`) und `ls` ausführen lassen (`Bash`). In `~/codex-hook-stdin.jsonl` notieren: `tool_name`, die Schlüssel in `tool_input`, ob `command` ein Text oder eine Liste ist und unter welchem Schlüssel der Patch steht. Danach Eintrag und beide Dateien wieder löschen.
- [ ] Fremdes Repo klonen: `git clone` eines Repos mit eigener `AGENTS.md` oder `SKILL.md` nach `projects/`. Warnt der Start der nächsten Session davor? Greift der Schutz auch beim Klonen selbst, oder erst beim nächsten Start?
- [ ] Workspace mit Leerzeichen im Pfad (z. B. `~/Mein Workspace`): Läuft die Einrichtung durch, und laufen beide Hooks (Warnung und Ablehnung wie oben)? Pfade in `hooks.json` und `allowlist.txt` in Anführungszeichen?
- [ ] Neues Projekt unter `projects/<name>/` (eigenes Git-Repo): Der Hook hält an, weil dort `AGENTS.md` entsteht. Nennt Codex die zwei Zeilen für `allowlist.txt`, und genügt es, sie selbst in `~/.codex/hooks/instruction-files/allowlist.txt` einzutragen?
- [ ] Neue Session in `projects/<name>/`: Kennt Codex den Namen, den Vault und die Regeln? Bringt `~/.codex/AGENTS.md` die Workspace-Regeln zuverlässig mit, auch wenn der Startordner ein anderer ist? (?) Frage zur Kontrolle: „Wo liegt der Fehlerbaum?“
- [ ] `$seal-session` am Ende einer Session: Session-Notiz in `30-Sessions/`, Eintrag im Fehlerbaum (falls etwas gefixt wurde) und `STAND.md` im Projekt richtig angelegt oder ergänzt?
- [ ] Zweite Einrichtung: Startet sie als Aktualisierung statt neues Interview? Bleibt ein weggefallener Bereich im Vault stehen, ohne gelöscht zu werden? Wird nichts doppelt in `config.toml`, `hooks.json` oder `allowlist.txt` eingetragen?
- [ ] Obsidian unter Mint: Installation über das `.deb`-Paket (`sudo apt install ./obsidian_*.deb`). Öffnet sich der Vault, stimmen Ordner, Vorlagen und Anhänge-Ordner?
- [ ] Gesamtdauer pro Schritt notiert (Vorprüfung, Interview, Plan, Erzeugen, Einstellungen, Hooks, Kontext, Prüfung)?

## Rückmeldung

Bitte kurz und konkret, Stichpunkte reichen.

- Codex-Version (`codex --version`):
- Mint-Version (`lsb_release -d`):
- Python-Version (`python3 --version`):
- Gesamtdauer:
- Lücken (was fehlt, was war unklar, wo musstest du raten):
- Fehler (Befehl, Meldung, Schritt):
- Verbesserungsvorschläge:
- Sonstiges:

## Ergebnisse

(je Lauf: Datum, System, Dauer pro Schritt, Probleme und was geändert wurde)
