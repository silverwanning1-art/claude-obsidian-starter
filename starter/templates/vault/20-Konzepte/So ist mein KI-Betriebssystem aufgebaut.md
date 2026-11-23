---
tags: [konzept, ki-betriebssystem]
status: aktiv
date: {{DATUM}}
---

# So ist mein KI-Betriebssystem aufgebaut

Mein KI-Betriebssystem ist ein Ordner auf meinem Laptop, den Workspace, mit meinem Wissen, meinen Regeln und meinen Projekten, und dazu {{AGENT_NAME}}, das darin arbeitet. Alles darin sind normale Textdateien.

## Kern

| Teil | Wofür | Wo es liegt |
|---|---|---|
| {{AGENT_NAME}} | arbeitet in meinen Ordnern: liest, schreibt, baut | das Programm auf meinem Laptop |
| Wissen | wer ich bin, was ich weiß, was schon gelöst ist | der Vault `{{VAULT}}/`, angezeigt in Obsidian |
| Regeln | wie wir zusammenarbeiten, in drei Ebenen: Workspace, Vault, Projekt | je eine `AGENTS.md` im Workspace, im Vault und in jedem Projekt |
| Rechte und Verbote | was {{AGENT_NAME}} darf und was nie (z. B. keine `.env`-Dateien lesen) | {{EINSTELLUNGEN}} |
| Hooks | kleine Programme, die anhalten, bevor fremde Anweisungsdateien entstehen | {{HOOKS_ORDNER}} |
| Skills | eingeübte Abläufe zum Aufrufen, z. B. {{SEAL}} am Ende einer Sitzung | {{SKILLS_ORDNER}} |
| Projekte | was ich baue, jedes mit eigenem Zeitstrahl (Git) | `projects/<name>/` |

## Welche Regeln gelten wann

Welche Regeln {{AGENT_NAME}} kennt, hängt vom Ordner ab, in dem die Sitzung startet. Deshalb starte ich zum Bauen eine neue Sitzung im Projektordner: Dann gelten zusätzlich die Regeln des Projekts, und {{AGENT_NAME}} liest zuerst dessen `STAND.md`.

Neben jeder `AGENTS.md` liegt eine `CLAUDE.md`, in der nur `@AGENTS.md` steht. Das ist ein Verweis, damit verschiedene KI-Programme dieselben Regeln lesen.

## Warum das wichtig ist

- Jede neue Sitzung kennt mich, ohne dass ich alles neu erkläre.
- Wissen steht an einem Ort und ist verknüpft, ich suche nicht mehr in alten Chats.
- Wechsle ich das Programm oder das Abo, bleibt alles da. Es sind meine Dateien.

## Grenzen

Verbote und Hooks erkennen feste Befehlsformen. Sie sind ein Sicherheitsnetz, kein Ersatz dafür, Vorschläge zu lesen, bevor ich zustimme.

## Verwandt

- [[Git in drei Begriffen]]
- [[40-Fehlerbaum/Index]]: hier schaue ich bei Fehlern zuerst
