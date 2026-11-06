# 0002: Einzelne Prüfungen aus icm-architect übernehmen

Status: angenommen, 2026-11-03

## Kontext

[icm-architect](https://github.com/RinDig/icm-architect) (MIT) baut Arbeitsordner nach der Interpretable Context Methodology: eine kurze `AGENTS.md`, die nur weiterleitet, Stand als Datei auf der Platte, neue Notizen als Kopie einer Vorlage. Das ist im Kern derselbe Aufbau wie in diesem Starter. Dort gibt es zusätzlich Prüfungen, die bei uns fehlten.

## Entscheidung

Übernommen, in eigenen Worten und auf Einsteiger zugeschnitten:

- **Kaltstart-Prüfung** am Ende der Einrichtung (dort „walk test“): Aus `AGENTS.md` und höchstens zwei weiteren Dateien muss klar sein, wo was liegt.
- **Links prüfen**: Ein Test löst alle Wikilinks der Vault-Vorlagen auf, die Einrichtung prüft die angelegten Dateien.
- **Groß- und Kleinschreibung**: Vor dem Anlegen wird geprüft, ob es den Namen schon in anderer Schreibweise gibt, weil Windows und macOS sonst still überschreiben.
- **Verschieben ins Archiv**: erst nach Verweisen suchen, bevorzugt in Obsidian verschieben (passt Links an), sonst kopieren, vergleichen, dann löschen.
- **Konzept-Vorlage** mit „Grenzen“ und „Quelle“, damit Einschränkungen und eigene Deutung getrennt vom Kern stehen.

Nicht übernommen: nummerierte Arbeitsstufen mit Vertrag je Ordner, „System map“, „Knowledge bundle from sources“ und per Skript erzeugte Indexdateien. Das ist für eine einstündige Einrichtung ohne Programmierkenntnisse zu viel Struktur, und der Setup-Skill kommt ohne Skripte aus.

## Folgen

- Die Einrichtung prüft am Ende mehr, dauert dadurch aber kaum länger.
- Kaputte Links in den Vorlagen fallen in der CI auf, nicht erst bei Teilnehmern.
- Die Ideen für Arbeitsstufen bleiben eine Option für einen späteren, optionalen Skill.
