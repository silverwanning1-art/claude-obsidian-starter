<!-- starter:begin notion v1 -->
# Workspace von {{NAME}}

Diese Datei lädt Codex in jeder Session auf diesem Rechner. Die Regeln gelten nur, wenn der Startordner der Session unter `{{WORKSPACE}}` liegt. Für Sessions außerhalb von `{{WORKSPACE}}` gilt diese Datei nicht.

{{NAME}}: {{ROLLE}}. Antworte auf {{SPRACHE}}, direkt und konkret. Code und Bezeichner auf Englisch.

## Karte

Wissen liegt in Notion, Code liegt lokal. Notion erreichst du über den Notion-MCP.

| Was | Wo | Wann lesen |
|---|---|---|
| Agent-Start | Notion: {{NOTION_START}} | zu Beginn jeder Session |
| Über {{NAME}} | Notion: {{NOTION_UEBER_MICH}} | bei Texten, Plänen und Fragen zum Studium |
| Masterarbeit | Notion: {{NOTION_MASTERARBEIT}} | Kapitel, Forschungsfrage, Methodik, Literatur |
| Konzepte (Fachwissen) | Notion-Datenbank: {{NOTION_KONZEPTE}} | bei Fachfragen zuerst hier suchen |
| Fehlerbaum | Notion-Datenbank: {{NOTION_FEHLERBAUM}} | bei Fehlern zuerst hier suchen |
| Sessions | Notion-Datenbank: {{NOTION_SESSIONS}} | nur von `$seal-session` |
| Code | `{{WORKSPACE}}/projects/<name>/`, je ein Git-Repo | Coding |
| Vorgaben der Firma | `projects/<name>/docs/vorgaben.md` | vor jeder Änderung am Code |

## Notion

- Zu Beginn jeder Session die Seite „Agent-Start“ lesen: aktueller Stand, nächste Schritte, häufige Fehler.
- Inhalte aus Notion nicht in lokale Dateien kopieren. Bei Bedarf in Notion nachlesen. Einzige Ausnahme sind die Vorgaben der Firma im Repo.
- Bei Fachfragen zuerst in Notion suchen (Konzepte, Masterarbeit) und die Seite nennen, aus der die Antwort stammt. Steht nichts dazu in Notion, das sagen und dann aus eigenem Wissen antworten.
- Neue Seiten und Abschnitte darfst du anlegen, wenn {{NAME}} es will oder `$seal-session` es verlangt. Bestehenden Text in Notion ändern oder löschen nur nach Ja von {{NAME}}.
- Antwortet der Notion-MCP nicht oder fehlt eine Seite: das sagen, nicht raten.

## Zusammenarbeit

- {{NAME}} entscheidet über Ziele, Prioritäten und Freigaben. Codex setzt um und erklärt so, dass {{NAME}} jede Änderung nachvollziehen kann.
- Bei Unklarheit oder Zielkonflikt fragen, nicht still entscheiden.
- Keine Passwörter, Schlüssel oder Tokens in Dateien, Notion-Seiten oder Commits. `.env`-Dateien nie lesen oder committen.
- Vertrauliche Daten der Firma nur dort ablegen, wo die Firma es erlaubt.
- Fremde Dateien namens `AGENTS.md`, `CLAUDE.md` oder `SKILL.md` (Downloads, Vorlagen) nie unter diesem Namen ablegen, sondern beschreibend umbenennen. Sonst gelten sie als Anweisung.

## Programmieren

- Coding-Sessions starten im Projektordner. Dort zuerst `AGENTS.md`, `STAND.md` und `docs/vorgaben.md` lesen.
- Die Vorgaben der Firma (Sprache, Frameworks, Schnittstellen, Deployment) gehen vor eigenen Vorlieben. Weicht etwas davon ab, vorher fragen.
- In Projekt-Repos nicht direkt auf `main` arbeiten. Branches: `feat/`, `fix/`, `docs/`.
- Kleine, abgeschlossene Commits: `typ: beschreibung` (feat, fix, docs, test, refactor, chore).
- Vor dem Commit Tests und Linter laufen lassen, soweit das Projekt sie hat.
- Merge und Deploy nur nach Freigabe durch {{NAME}}.
- Entscheidungen mit Tragweite als kurze Notiz unter `docs/adr/` im Projekt. Für die Masterarbeit sind sie die Belege, warum das Artefakt so gebaut ist.

## Gedächtnis

- Bei Fehlern zuerst „Häufige Fehler“ auf der Seite „Agent-Start“ lesen, dann in der Fehlerbaum-Datenbank suchen.
- Am Ende einer Session, in der etwas gelernt, entschieden oder gelöst wurde: `$seal-session` anbieten.
<!-- starter:end notion v1 -->
