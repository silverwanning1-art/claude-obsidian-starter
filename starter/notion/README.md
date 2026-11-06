# Variante: Notion statt Obsidian (Codex)

Für alle, deren Wissen schon in Notion liegt. Notion bleibt das Gedächtnis, lokal kommt nur die Coding-Umgebung dazu. Nichts wird aus Notion kopiert: Codex liest und schreibt Notion über den Notion-MCP (eine Schnittstelle, über die Codex auf Notion zugreift).

Diese Variante läuft **ohne** die Einrichtung mit „los“. Den entpackten Starter also nicht als Workspace öffnen, sonst startet die Einrichtung für Obsidian. Die Schritte unten erledigst du von Hand oder lässt sie Codex in einem anderen Ordner Schritt für Schritt ausführen.

## Aufbau

| Was | Wo |
|---|---|
| Regeln für Codex, Karte der Notion-Seiten | `~/.codex/AGENTS.md` (aus `codex-AGENTS.template.md`) |
| Skill zum Abschließen einer Session | `~/.agents/skills/seal-session/SKILL.md` (aus `seal-session.SKILL.template.md`) |
| Code | `~/workspace/projects/<name>/`, je ein Git-Repo |
| Vorgaben der Firma für ein Projekt | `projects/<name>/docs/vorgaben.md` im Repo |
| alles andere | Notion |

Die Regeln stehen in `~/.codex/AGENTS.md`, weil Codex `AGENTS.md` nur dort und im Projekt-Repo liest, nicht in übergeordneten Ordnern wie `~/workspace/`. Sie gelten nur für Sessions unter `~/workspace/`.

## Notion-Struktur

Bestehende Seiten bleiben, wo sie sind. Die Karte in `~/.codex/AGENTS.md` verweist auf sie. Neu anlegen musst du nur, was fehlt.

| Seite oder Datenbank | Inhalt | Felder (nur Datenbanken) |
|---|---|---|
| **Agent-Start** (Seite) | Abschnitte „Stand“, „Häufige Fehler“ (höchstens 15 Zeilen: `Symptom -> Ursache -> Lösung`), „Inbox“. Codex liest sie zu Beginn jeder Session | – |
| **Über mich** (Seite) | Rolle, Studium, Betreuung, Firma, Schreibstil | – |
| **Masterarbeit** (Seite) | Forschungsfrage, Gliederung, Kapitel, Literatur, Absprachen | – |
| **Konzepte** (Datenbank) | Fachwissen, ein Eintrag je Begriff, im Text: Kern, Grenzen, Quelle, Offen | Bereich, Status (`Entwurf`, `geklärt`) |
| **Fehlerbaum** (Datenbank) | ein Eintrag je Fehler, Titel ist das Symptom | Ursache, Lösung, Projekt, Status (`vermutet`, `geprüft`), Zuletzt (Datum) |
| **Sessions** (Datenbank) | ein Eintrag je versiegelter Session | Datum, Typ (`coding`, `schreiben`, `klärung`, `gemischt`), Projekt |

Den Zugriff des Notion-MCP auf die Seiten beschränken, die Codex braucht.

## Einrichten

1. **Notion-MCP in Codex eintragen** und anmelden. Den genauen Befehl in der aktuellen Doku von Codex und Notion nachsehen, er ändert sich gelegentlich. Prüfen: Codex fragen „Lies die Seite Agent-Start“.
2. **Notion-Struktur** wie oben anlegen und von jeder Seite und Datenbank den Link kopieren („Link kopieren“ im Menü der Seite).
3. **Ordner** `~/workspace/projects/` anlegen.
4. **Regeln:** `codex-AGENTS.template.md` nach `~/.codex/AGENTS.md` kopieren und die Platzhalter ersetzen: `{{NAME}}`, `{{ROLLE}}`, `{{SPRACHE}}`, `{{WORKSPACE}}` (absoluter Pfad, z. B. `/Users/anna/workspace`) und die Notion-Links `{{NOTION_…}}`. Gibt es `~/.codex/AGENTS.md` schon, den Text zwischen den Markern unten anhängen, nichts ersetzen.
5. **Skill:** `seal-session.SKILL.template.md` als `~/.agents/skills/seal-session/SKILL.md` ablegen. Gibt es dort schon einen `seal-session`, vorher ansehen und nicht ungefragt überschreiben.
6. **Codex-Einstellungen** (empfohlen): `../templates/codex-config-fragment.toml` in `~/.codex/config.toml` ergänzen (Codex darf in `~/workspace` schreiben) und `../templates/codex-starter.rules` nach `~/.codex/rules/starter.rules` kopieren (verbietet `git push --force` und `rm -rf`). Platzhalter `{{WORKSPACE}}` ersetzen.
7. **Projekt** anlegen: `projects/<name>/` mit `git init`, einer `AGENTS.md` mit Stack, Testbefehl und Verweis auf `docs/vorgaben.md`, einer `STAND.md` aus `../templates/STAND.template.md` und `docs/vorgaben.md` mit den Vorgaben der Firma.

Optional schützt `../hooks/instruction-files/` vor fremden Anweisungsdateien, siehe dortige README.

## Prüfen

Codex beenden, in `~/workspace/projects/<name>/` neu starten und fragen:

- „Welche AGENTS.md-Dateien hast du geladen?“ Erwartet: `~/.codex/AGENTS.md` und die des Projekts.
- „Was steht auf Agent-Start?“ Erwartet: der Inhalt aus Notion.
- „Welche Vorgaben gelten für dieses Projekt?“ Erwartet: der Inhalt von `docs/vorgaben.md`.

Am Ende der ersten echten Session `$seal-session` ausprobieren und in Notion nachsehen, ob Session-Eintrag und „Stand“ stimmen.
