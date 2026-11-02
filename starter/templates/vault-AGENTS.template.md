<!-- starter:begin v1 -->
# Vault

Zweites Gehirn von {{NAME}}. Allgemeine Regeln (Sprache, Zusammenarbeit, Fehlerbaum) stehen in der `AGENTS.md` eine Ebene höher. Hier stehen nur die Konventionen für Notizen. Die `CLAUDE.md` daneben enthält nur `@AGENTS.md` und verweist auf diese Datei.

Wer {{NAME}} ist und woran {{NAME}} arbeitet: [[00-Kontext/Über mich]]. Schreibstil: [[00-Kontext/Schreibstil]]. Lesen, wenn die Aufgabe es braucht (Texte, Angebote, Pläne), nicht bei jeder Anfrage.

## Struktur

| Ordner | Inhalt |
|---|---|
| `00-Kontext/` | Über mich, Zielgruppe, Angebot, Schreibstil, Arbeitsstil |
{{BEREICHE_ZEILEN}}
| `20-Konzepte/` | Ideen, Methoden und Wissen zum Ausarbeiten, auch Ideen für Projekte, bevor sie umgesetzt werden |
| `30-Sessions/` | Zusammenfassungen abgeschlossener Sessions, Skill {{SEAL}}, Dateiname `JJJJ-MM-TT Thema.md` |
| `40-Fehlerbaum/` | `Index.md` (kurz, bei Fehlern zuerst lesen) und `Eintraege/` (ausführlich) |
| `90-Archiv/` | Abgeschlossenes. Nur auf Anweisung von {{NAME}} hierher verschieben |
| `Templates/`, `Attachments/` | Vorlagen, Anhänge (Bilder, PDFs) |
| `Inbox.md` | Sammelstelle für alles ohne klaren Platz |

## Konventionen für Notizen

- Verknüpfen mit `[[Wikilinks]]`. Vor dem Anlegen einer Notiz prüfen, ob es schon eine passende gibt, und diese ergänzen.
- Frontmatter in YAML: `tags`, `status`, `date`.
- Dateinamen normal mit Leerzeichen. Keine Emojis.
- Ein Konzept ist eine einzelne Datei in `20-Konzepte/`, ein Unterordner erst bei mehreren Dateien.
- Code-Projekte dokumentieren sich im eigenen Repo unter `projects/`, nicht im Vault.
- Keine vertraulichen Firmendaten (Kundendaten, Verträge, interne Zahlen), solange die Firma die Nutzung von {{AGENT_NAME}} dafür nicht freigegeben hat.

## „Merk dir das“

Thematisch passend ablegen: über {{NAME}} in [[00-Kontext/Über mich]], Schreibregeln in [[00-Kontext/Schreibstil]], Wünsche an die Zusammenarbeit in [[00-Kontext/Arbeitsstil]], Regeln für den Vault in diese Datei, Fehler mit Ursache und Lösung in den Fehlerbaum.
<!-- starter:end v1 -->
