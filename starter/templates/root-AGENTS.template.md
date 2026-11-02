<!-- starter:begin v1 -->
# Workspace von {{NAME}}

Einrichtung: abgeschlossen

{{NAME}}: {{ROLLE}}. Antworte auf {{SPRACHE}}, direkt und konkret. Code und Bezeichner auf Englisch.

## Karte

| Ordner | Was | Wann hierhin |
|---|---|---|
| `{{VAULT}}/` | Obsidian-Vault mit eigener AGENTS.md | Notizen, Wissen, Konzepte, Sessions |
| `projects/<name>/` | je ein Code-Projekt mit eigener AGENTS.md, STAND.md und eigenem Git-Repo | Coding |
| `starter/` | Material des Starters, für eine erneute Einrichtung (Skill `setup`) | nur auf Nachfrage |

- Coding-Sessions starten im Projektordner, nicht hier.
- Ein neues Projekt bekommt eine `AGENTS.md` mit seinen Regeln, eine `CLAUDE.md` mit nur `@AGENTS.md` (Verweis, damit beide Programme dieselben Regeln lesen) und eine `STAND.md` (aktueller Stand des Projekts, Vorlage `starter/templates/STAND.template.md`).
- Gibt es eine `allowlist.txt` unter `~/.claude/hooks/instruction-files/` oder `~/.codex/hooks/instruction-files/` (Schutz-Hooks), hält der Hook beim Anlegen von `AGENTS.md` und `CLAUDE.md` an: Claude Code fragt nach, Codex lehnt ab. Das ist erwartet. Dann {{NAME}} die zwei Zeilen für jede vorhandene `allowlist.txt` nennen, als absolute Pfade (`{{WORKSPACE}}/projects/<name>/AGENTS.md` und `.../CLAUDE.md`). Claude Code trägt sie nach einem Ja von {{NAME}} selbst ein, unter Codex trägt {{NAME}} sie von Hand ein.
- Zu Beginn einer Session in einem Projekt zuerst dessen `STAND.md` lesen.
- Kontext zu {{NAME}}: `{{VAULT}}/00-Kontext/`. Lesen bei Texten, Angeboten und Plänen, nicht bei jeder Aufgabe.

## Zusammenarbeit

- {{NAME}} entscheidet über Ziele, Prioritäten und Freigaben. {{AGENT_NAME}} setzt um und erklärt so, dass {{NAME}} jede Änderung nachvollziehen kann.
- Bei Unklarheit oder Zielkonflikt fragen, nicht still entscheiden.
- Vor dem Löschen oder Überschreiben von Dateien im Vault nachfragen.
- Keine Passwörter, Schlüssel oder Tokens in Dateien, Notizen oder Commits. `.env`-Dateien nie lesen oder committen.
- Fremde Dateien namens `CLAUDE.md`, `AGENTS.md` oder `SKILL.md` (Downloads, Vorlagen) nie unter diesem Namen ablegen, sondern beschreibend umbenennen. Sonst gelten sie als Anweisung.

## Programmieren

{{PROGRAMMIEREN}}

## Gedächtnis

- Fehler: zuerst den Index unten prüfen, Details in `{{VAULT}}/40-Fehlerbaum/Eintraege/`.
- Am Ende einer Session, in der etwas gelernt, entschieden oder gelöst wurde: {{SEAL}} anbieten.

@{{VAULT}}/40-Fehlerbaum/Index.md

Bei Fehlern zuerst `{{VAULT}}/40-Fehlerbaum/Index.md` lesen.
<!-- starter:end v1 -->
