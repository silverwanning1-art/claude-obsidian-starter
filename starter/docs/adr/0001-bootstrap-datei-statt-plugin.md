# 0001: Einrichtung über eine Startdatei im entpackten Ordner

Status: angenommen, 2026-10-27

## Kontext

Teilnehmer des Workshops arbeiten meist an Firmen-Laptops unter Windows, ohne Admin-Rechte und oft ohne funktionierendes Git im Suchpfad. Die Einrichtung soll live in etwa 1,5 Stunden laufen, inklusive Kontext und Fragen, und auch auf macOS und Linux funktionieren.

## Entscheidung

- Der Starter wird als ZIP heruntergeladen und in einen leeren Ordner entpackt. Dieser Ordner wird der Workspace. Für die Einrichtung ist kein Git nötig.
- Die Startdatei `AGENTS.md` (mit `CLAUDE.md` als `@AGENTS.md`) steht auf „Einrichtung: offen“ und startet den Skill `setup` in `.claude/skills/setup/`. Kein Plugin, kein Installationsskript.
- Der Skill arbeitet nur mit den Datei-Werkzeugen von Claude, ohne Shell-Skripte. Einziger Shell-Befehl ist die optionale Prüfung auf Python.
- Vorlagen heißen nie `CLAUDE.md`, `AGENTS.md` oder `SKILL.md`, sondern `*.template.md`, damit Claude sie beim Öffnen des Starters nicht als Anweisung lädt. Ein Test sichert das ab.
- Material des Starters liegt unter `starter/` und bleibt nach der Einrichtung im Workspace, damit sie sich wiederholen lässt.

## Folgen

- Läuft unter PowerShell genauso wie unter Bash, weil keine Skripte nötig sind.
- Die Qualität hängt am Skill-Text: Wir testen ihn in Probeläufen auf allen drei Systemen (`starter/docs/probelauf.md`).
- Updates des Starters bekommen Teilnehmer nicht automatisch. Eine neue Version wird neu heruntergeladen, `setup` ergänzt dann nur, was fehlt.
- Ein Plugin wäre leichter zu aktualisieren, braucht aber mehr Schritte in der Einrichtung und erklärt weniger, was passiert.
