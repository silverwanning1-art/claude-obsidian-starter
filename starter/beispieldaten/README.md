# Beispieldaten für das Dashboard

Zwei CSV-Dateien mit demselben Aufbau, für den Workshop „Vibe-Coding im Unternehmen“.

| Datei | Zeitraum | Wofür |
|---|---|---|
| `teil1_bis_2025-12.csv` | Januar 2019 bis Dezember 2025 | Dashboard bauen |
| `teil2_2026-01_bis_heute.csv` | Januar bis September 2026 | Dashboard aktualisieren |

## Inhalt

- Produktionsindex der Industrie, Monatswerte, saison- und kalenderbereinigt
- 7 Länder (Deutschland, Österreich, Frankreich, Italien, Spanien, Niederlande, Polen) und die EU27
- Industrie gesamt und 8 Branchen
- Spalten: `monat`, `land_code`, `land`, `branche_code`, `branche`, `produktionsindex`

## Lesen

Der Index ist keine Euro- und keine Stückzahl. 100 ist die Produktion im Monatsdurchschnitt 2021. 92,4 heißt also 7,6 % weniger als 2021. Er zeigt die Entwicklung, nicht die Größe eines Landes.

Manche Werte fehlen ganz, die Zeile gibt es dann nicht: Spanien und Italien bei Nahrung, Getränke und Tabak (`C10-C12`), die Niederlande bei Elektronik (`C26`) im Jahr 2021 und beim Maschinenbau (`C28`) im Dezember 2021. Im Dashboard sind das Lücken, keine Nullen.

## Mögliche Fragestellungen

Für alle ohne eigene Idee, als Einstieg:

- Wie steht die deutsche Autoindustrie im EU-Vergleich da?
- Welche Branchen haben sich seit Corona erholt, welche nicht?
- Wo liegt Polen im Vergleich zu Deutschland und Frankreich?

## Quelle

Eurostat, Datensatz `sts_inpr_m` (Production in industry, monthly data), Lizenz CC BY 4.0.
