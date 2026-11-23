---
tags: [konzept, git]
status: aktiv
date: {{DATUM}}
---

# Git in drei Begriffen

Git ist der Zeitstrahl eines Projekts: Es merkt sich jeden gesicherten Stand, und ich kann jederzeit zu einem früheren zurück.

## Kern

| Begriff | Bild | So frage ich {{AGENT_NAME}} |
|---|---|---|
| **Commit** | ein Punkt auf dem Zeitstrahl, ein gesicherter Stand mit kurzer Beschreibung | „Sichere den Stand.“ / „Zeig mir meinen Zeitstrahl.“ / „Geh zurück zum Stand vor dem Update.“ |
| **Branch** | eine Kopie des Zeitstrahls, auf der ich Neues ausprobiere, ohne den Hauptstrahl (`main`) und damit meine Kollegen zu stören | „Mach mir einen Branch und bau darauf …“ |
| **Merge** | die Entwicklung vom Branch zurück in den Hauptstrahl holen, damit alle sie nutzen können | „Übernimm den Branch in main.“ |

Im Team läuft der Merge meist über einen **Pull Request (PR)** auf GitHub: Kollegen sehen sich die Änderung an, und eine automatische Prüfung testet, dass nichts kaputtgeht. Erst wenn alles grün ist, wird gemergt.

## Was in den Zeitstrahl gehört

Git versioniert jede Datei, die ich committe, Code genauso wie Daten.

- Code: ja
- kleine Beispieldaten: unbedenklich
- echte Firmendaten: eher nicht, spätestens wenn das Projekt auf GitHub liegt
- `.env`-Dateien, Passwörter, Schlüssel: nie

Was nicht hinein soll, steht in der Datei `.gitignore` im Projekt.

## Grenzen

Ein Commit sichert nur auf meinem Laptop. Erst ein Push auf einen Server wie GitHub ist eine Sicherung außerhalb.

## Verwandt

- [[So ist mein KI-Betriebssystem aufgebaut]]
