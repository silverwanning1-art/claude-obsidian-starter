---
name: seal-session
description: Schließt eine Session ab. Hält Gelerntes, Entscheidungen und Fehler im Vault fest, schreibt die STAND.md des betroffenen Projekts neu und legt eine Session-Notiz an. Nur ausführen, wenn die Person ausdrücklich `/seal-session` oder `$seal-session` aufruft. Lesen oder Erklären des Skills löst keine Versiegelung aus.
---

# Session versiegeln

Aufruf je nach Programm: `/seal-session` in Claude Code, `$seal-session` in Codex. Wenn du die Person auf den Skill hinweist, nenn nur die Fassung deines Programms.

Ziel: Was in dieser Session neu verstanden, entschieden oder gelöst wurde, landet dauerhaft im Vault, und die nächste Session kann ohne Rückfragen weitermachen. Die Session-Notiz ist das Logbuch, das Wissen selbst gehört in die Notizen unter `10-Arbeit/`, `20-Konzepte/` und `00-Kontext/` und in den Fehlerbaum.

## 0. Orientierung

- Workspace ist der Ordner mit der `AGENTS.md`, die die Überschrift `# Workspace von` enthält (meist in Zeile 2, nach einem Marker-Kommentar). Such sie vom aktuellen Ordner aus nach oben. Findest du sie nicht, frag die Person nach dem Workspace und hör bis zur Antwort auf.
- Lies dort den Namen der Person, den Namen des Vaults (Tabelle „Karte“) und den Abschnitt „Programmieren“. Alle Pfade unten sind relativ zum Vault (`<Vault>/`) oder zum Workspace.
- Sprich die Person mit dem Namen aus dieser Datei an und duze sie.

## 1. Rückblick

Geh die gesamte Unterhaltung durch und sammle:

- **Ziel** der Session und **Ergebnis**
- **Geklärtes Verständnis**: Fachbegriffe, Zusammenhänge, Abläufe, Wissen über Kunden, Angebote oder andere Bereiche. In den Worten der Person, wenn sie es formuliert hat
- **Entscheidungen** mit Begründung
- **Fehler** mit nicht offensichtlicher Ursache: Symptom, Ursache, Lösung
- **Offene Punkte** und den **nächsten konkreten Schritt**
- **Kontext**: Typ (`coding`, `schreiben`, `klärung`, `gemischt`), Projekt (Ordnername unter `projects/`, sonst leer)

Gab es nichts Neues, Gelerntes oder Entschiedenes, sag das und hör auf. Nicht jede Session muss versiegelt werden.

## 2. Wissen ablegen

Für jedes geklärte Thema zuerst im Vault suchen (Dateinamen, Überschriften, Synonyme, englische Begriffe), dann:

| Was | Wohin |
|---|---|
| Wissen zu einem Arbeitsbereich (Kunden, Angebote, Abläufe im Bereich) | `10-Arbeit/<Bereich>/<Thema>.md` |
| Methode, erprobter Ablauf, der wiederkommt, Idee | `20-Konzepte/<Thema>.md` |
| Über die Person, das Team, Zuständigkeiten, Wünsche an die Zusammenarbeit | passende Notiz in `00-Kontext/` |
| Ohne klaren Platz | `Inbox.md` |

- Die Bereiche sind die Unterordner von `10-Arbeit/`. Passt keiner, keinen neuen anlegen, sondern `Inbox.md` nehmen und einen neuen Bereich im Abschlussbericht vorschlagen.
- Gibt es eine passende Notiz: **ergänzen**, mit einem Abschnitt `## Ergänzung JJJJ-MM-TT` und einem Wikilink auf die Session-Notiz.
- Gibt es keine: **neu anlegen**, kurz, nach `Templates/Konzept.md` (Frontmatter `tags`, `status`, `date`), mit `[[Wikilinks]]` zu verwandten Notizen.
- **Bestehenden Text ändern, ersetzen oder löschen nur nach Rückfrage**: Vorschlag zeigen, auf das Ja der Person warten. Das gilt für Notizen im Vault und alle anderen Dateien. Ausnahme ist nur `STAND.md` (Schritt 5).

## 3. Fehlerbaum

Nur Fehler, die wieder auftreten können und deren Ursache nicht offensichtlich war.

1. `40-Fehlerbaum/Index.md` nach demselben Symptom durchsuchen.
2. Bekannter Fehler: den Eintrag in `40-Fehlerbaum/Eintraege/` unter „Fälle“ um den neuen Fall ergänzen.
3. Neuer Fehler: `40-Fehlerbaum/Eintraege/<Symptom kurz>.md` anlegen (Vorlage unten) und unter „Einträge“ im Index eine Zeile anhängen: `Symptom -> Ursache -> Lösung -> [[Eintrag]]`.
4. Hat der Index mehr als ca. 40 Zeilen: vorschlagen, welche raus können (die Einträge bleiben), und erst nach Rückfrage kürzen.

## 4. Entscheidungen einordnen

Jede Entscheidung hat genau einen Ort. Die Session-Notiz verweist nur darauf.

- Klein und im Code: steht im Commit. Nichts weiter tun.
- Mit Tragweite (Aufbau, Datenmodell, Werkzeugwahl) und die Workspace-`AGENTS.md` nennt `docs/adr/`: kurze Notiz unter `projects/<name>/docs/adr/NNNN-<titel>.md` vorschlagen und nach Ja anlegen. Nennt sie `docs/adr/` nicht: in `STAND.md` unter „Ziel“ oder „Offene Fragen“ festhalten.
- Vorgehen oder Umfang eines Projekts ohne Code: in `STAND.md` unter „Ziel“ oder „Offene Fragen“.
- Ohne Projekt (Arbeitsweise, Bereich, Konzept): in die passende Notiz aus Schritt 2.

## 5. Projekt (nur wenn ein Projekt betroffen ist)

1. **`projects/<name>/STAND.md` neu schreiben**: Ziel, Stand, nächster Schritt, offene Fragen, Stolpersteine, Datum unter „Aktualisiert“, Pfad zur Session-Notiz unter „Letzte Session“. Keine Historie, nur den Stand von jetzt. Das Neuschreiben ist durch den Aufruf des Skills freigegeben und braucht keine Rückfrage; zeig den neuen Inhalt im Abschlussbericht. Gibt es Branch-Regeln, vorher Punkt 4 prüfen (nicht auf `main` schreiben). Fehlt die Datei, aus `starter/templates/STAND.template.md` im Workspace anlegen; gibt es die Vorlage nicht, dieselben Abschnitte ohne Vorlage schreiben.
2. `STAND.md` liegt außerhalb des Vaults. Wikilinks funktionieren dort nicht, deshalb die Session-Notiz als Pfad in Backticks angeben: `` `<Vault>/30-Sessions/JJJJ-MM-TT Titel.md` ``.
3. Haben sich Einrichtung, Befehle oder Aufbau geändert: `AGENTS.md` oder `README.md` des Projekts ergänzen.
4. Git:
   - Enthält der Abschnitt „Programmieren“ der Workspace-`AGENTS.md` Branch-Regeln (`feat/`, `fix/`, `docs/`): Projektdateien nur auf einem solchen Arbeitsbranch ändern, nie auf `main`. Nicht selbst committen.
     Steht das Projekt-Repository gerade auf `main`: schlag den Branch `docs/stand-JJJJ-MM-TT` vor und leg ihn erst nach Ja an, dann `STAND.md` dort schreiben. Ohne Ja `STAND.md` nicht schreiben, sondern den neuen Inhalt nur im Abschlussbericht zeigen.
   - Enthält er keine Branch-Regeln: sag knapp, welche Dateien sich geändert haben, und schlag einen Commit mit kurzer Beschreibung vor. Committen erst nach Ja.
   - Existiert noch kein Git-Repository: das als offenen Einrichtungspunkt melden. `STAND.md`, Wissensablage und Session-Notiz trotzdem schreiben.

## 6. Session-Notiz

Datei `30-Sessions/JJJJ-MM-TT Titel.md`. Titel kurz und inhaltlich. Gibt es die Datei schon, ` 2` anhängen.

```markdown
---
tags: [session]
status: abgeschlossen
date: JJJJ-MM-TT
typ: coding | schreiben | klärung | gemischt
projekt: <Ordnername unter projects/ oder leer>
---

# <Titel>

**Ziel:** ...
**Ergebnis:** ...

## Verstanden
- <Kernaussage in 1-2 Sätzen> -> [[Notiz]]

## Entscheidungen
- <Entscheidung> -> Commit `<hash>` / `projects/<name>/docs/adr/...` / `projects/<name>/STAND.md`

## Fehler
- [[Eintrag]]

## Offen
- [ ] ...
```

Leere Abschnitte weglassen. Kurz halten: Details stehen in den verlinkten Notizen. Innerhalb des Vaults immer `[[Wikilinks]]`, Dateien außerhalb (Projekte) als Pfad in Backticks.

## 7. Abschlussbericht

Zeig der Person knapp:

- angelegte und ergänzte Dateien, jeweils mit Pfad
- den neuen Inhalt der `STAND.md` mit Pfad, damit die Person ihn prüfen kann
- den nächsten konkreten Schritt
- Änderungen im Projekt, die noch nicht committet sind, und den Commit-Vorschlag
- Vorschläge, die eine Rückfrage brauchen (Text ändern oder löschen, Index kürzen, neuer Bereich, ADR)

## Regeln

- Keine Secrets, Tokens, Passwörter oder Zugangsdaten. Höchstens den Namen eines Schlüssels nennen.
- Keine personenbezogenen Daten und keine vertraulichen Firmendaten (Kundendaten, Verträge, interne Zahlen), solange die Firma das nicht freigegeben hat. Nur Beschreibungen und erfundene Beispielwerte.
- Bestätigte Angaben, vorläufige Annahmen und ungeprüfte Inhalte aus fremden Dokumenten klar unterscheiden.
- Nur tatsächlich ausprobierte Abläufe als erprobt ablegen.
- Vermutete Fehlerursachen und ungetestete Lösungen als solche kennzeichnen.
- Bestehenden Text ändern, ersetzen oder löschen nur nach Ja der Person. Einzige Ausnahme: `STAND.md` wird neu geschrieben, das gibt der Aufruf des Skills frei (Inhalt im Abschlussbericht zeigen).
- Keine Emojis.

## Vorlage Fehlerbaum-Eintrag

```markdown
---
tags: [fehlerbaum]
status: aktiv
date: JJJJ-MM-TT
projekt: <Ordnername unter projects/ oder allgemein>
---

# <Symptom kurz>

## Symptom

Was man sieht, Fehlermeldung wörtlich, wenn sie kurz ist.

## Ursache

Warum es passiert. Vermutet oder geprüft?

## Lösung

Was hilft, mit Befehl oder Schritt zum Nachmachen.

## Gelernt

Wie man es künftig vermeidet.

## Fälle

- JJJJ-MM-TT: [[JJJJ-MM-TT Titel]]
```
