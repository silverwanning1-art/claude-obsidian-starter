# claude-obsidian-starter

Ein Starter, mit dem dein KI-Assistent (Claude Code oder Codex) dir in etwa einer Stunde ein eigenes KI-Betriebssystem einrichtet: einen Obsidian-Vault als Gedächtnis, einen Ordner für Code-Projekte und kurze Regeln, nach denen er mit dir arbeitet. Entstanden für den Workshop „Vibe-Coding im Unternehmen“.

**Start in einem Satz:** Starter als ZIP herunterladen, in einen leeren Ordner außerhalb von OneDrive, iCloud oder Dropbox entpacken, den Ordner in Claude Code oder Codex öffnen und „los“ schreiben.

## Was du brauchst

- ein Abo mit Claude Code (mindestens Pro) oder ein ChatGPT-Konto mit Codex
- Claude Code oder Codex, dazu Obsidian, installiert
- für den Coding-Teil zusätzlich Git und Python

Die genauen Schritte für Windows, macOS und Linux stehen in der [Vorab-Checkliste](starter/handout/Vorab-Checkliste.md).

## Was die Einrichtung macht

1. Sie prüft den Ordner (Cloud-Speicher, bestehender Vault, Betriebssystem).
2. Sie stellt dir einzeln ein paar Fragen: Name, Rolle, Bereiche, Projekte.
3. Sie zeigt dir den Plan als Baum und wartet auf dein Ja.
4. Sie legt den Vault, den Ordner `projects/` und die Regeln an.
5. Mit deiner Zustimmung ergänzt sie die Einstellungen von Claude Code oder Codex (Berechtigungen, Skills, optional Schutz-Hooks). Vorher zeigt sie dir, was sich ändert.
6. Zum Schluss füllst du mit deinem Assistenten deinen Kontext aus (über dich, Zielgruppe, Angebot, Schreibstil). Das kannst du auch später allein machen.

Bestehende Dateien werden nie überschrieben. Die Einrichtung lässt sich wiederholen.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `AGENTS.md`, `CLAUDE.md` | Startdatei, wird bei der Einrichtung durch deine Regeln ersetzt |
| `.claude/skills/setup/` | der Einrichtungs-Skill für Claude Code |
| `.agents/skills/setup/` | derselbe Skill für Codex (Kopie) |
| `starter/templates/` | Vorlagen für Regeln, Vault und Einstellungen |
| `starter/skills/` | Skills, die bei der Einrichtung installiert werden |
| `starter/hooks/` | Schutz vor fremden Anweisungsdateien |
| `starter/notion/` | Variante mit Notion statt Obsidian, für Codex, Einrichtung von Hand |
| `starter/handout/` | Handout, Vorab-Checkliste, Troubleshooting |
| `starter/docs/` | Entscheidungen (ADR) und Probeläufe |

## Lizenz

MIT, siehe [LICENSE](LICENSE).
