---
name: seal-session
description: Schließt eine Session ab. Hält Gelerntes, Entscheidungen und Fehler in Notion fest, schreibt die STAND.md des betroffenen Projekts neu und legt einen Session-Eintrag in Notion an. Nur ausführen, wenn die Person ausdrücklich `$seal-session` aufruft. Lesen oder Erklären des Skills löst keine Versiegelung aus.
---

# Session versiegeln (Notion)

Ziel: Was in dieser Session neu verstanden, entschieden oder gelöst wurde, landet dauerhaft in Notion, und die nächste Session kann ohne Rückfragen weitermachen. Der Session-Eintrag ist das Logbuch. Das Wissen selbst gehört in die Konzepte, die Masterarbeit, „Über mich“ und den Fehlerbaum.

## 0. Orientierung

- Die Regeln aus `~/.codex/AGENTS.md` (Überschrift `# Workspace von`) sind geladen. Lies dort den Namen der Person, den Workspace-Pfad und die Tabelle „Karte“ mit den Notion-Links. Fehlt die Datei oder die Karte, sag das und hör auf.
- Prüfe, ob der Notion-MCP antwortet (Seite „Agent-Start“ abrufen). Antwortet er nicht: sag das, zeig alles, was du ablegen wolltest, im Abschlussbericht und schreib nur `STAND.md` (Schritt 5).
- Sprich die Person mit ihrem Namen an und duze sie.

## 1. Rückblick

Geh die gesamte Unterhaltung durch und sammle:

- **Ziel** der Session und **Ergebnis**
- **Geklärtes Verständnis**: Fachbegriffe, Zusammenhänge, Methoden, Wissen zur Masterarbeit. In den Worten der Person, wenn sie es formuliert hat
- **Entscheidungen** mit Begründung
- **Fehler** mit nicht offensichtlicher Ursache: Symptom, Ursache, Lösung
- **Offene Punkte** und den **nächsten konkreten Schritt**
- **Kontext**: Typ (`coding`, `schreiben`, `klärung`, `gemischt`), Projekt (Ordnername unter `projects/`, sonst leer)

Gab es nichts Neues, Gelerntes oder Entschiedenes, sag das und hör auf. Nicht jede Session muss versiegelt werden.

## 2. Wissen ablegen

Für jedes geklärte Thema zuerst in Notion suchen (Titel, Synonyme, englische Begriffe), dann:

| Was | Wohin |
|---|---|
| Fachbegriff, Methode, Zusammenhang | Konzepte-Datenbank: ein Eintrag je Begriff |
| Inhalt der Masterarbeit (Forschungsfrage, Kapitel, Literatur, Absprachen mit Betreuung oder Firma) | passende Seite unter „Masterarbeit“ |
| Über die Person, Wünsche an die Zusammenarbeit | Seite „Über mich“ |
| Ohne klaren Platz | Abschnitt „Inbox“ auf der Seite „Agent-Start“ |

- Gibt es eine passende Seite: **ergänzen**, unten mit der Überschrift `Ergänzung JJJJ-MM-TT` und einem Link auf den Session-Eintrag.
- Gibt es keine: **neu anlegen**, kurz, mit den Abschnitten Kern, Grenzen, Quelle, Offen. Unter Quelle steht, woher das Wissen stammt (Literatur, Gespräch, eigene Herleitung).
- **Bestehenden Text ändern, ersetzen oder löschen nur nach Rückfrage**: Vorschlag zeigen, auf das Ja der Person warten. Einzige Ausnahmen sind `STAND.md` (Schritt 5) und der Abschnitt „Stand“ auf „Agent-Start“ (Schritt 6).

## 3. Fehlerbaum

Nur Fehler, die wieder auftreten können und deren Ursache nicht offensichtlich war.

1. In der Fehlerbaum-Datenbank nach demselben Symptom suchen.
2. Bekannter Fehler: im Eintrag unter „Fälle“ das Datum und den Link zum Session-Eintrag ergänzen, das Feld „Zuletzt“ setzen.
3. Neuer Fehler: Eintrag anlegen. Titel ist das Symptom kurz. Felder: Ursache, Lösung, Projekt, Status (`vermutet` oder `geprüft`), Zuletzt. Im Text: Symptom mit Fehlermeldung, Ursache, Lösung zum Nachmachen, Gelernt, Fälle.
4. Tritt der Fehler oft auf oder kostet er viel Zeit: vorschlagen, ihn als eine Zeile unter „Häufige Fehler“ auf „Agent-Start“ aufzunehmen (`Symptom -> Ursache -> Lösung`). Erst nach Ja. Die Liste bleibt unter 15 Zeilen.

## 4. Entscheidungen einordnen

Jede Entscheidung hat genau einen Ort. Der Session-Eintrag verweist nur darauf.

- Klein und im Code: steht im Commit. Nichts weiter tun.
- Mit Tragweite für das Artefakt (Aufbau, Datenmodell, Werkzeugwahl): kurze Notiz unter `projects/<name>/docs/adr/NNNN-<titel>.md` vorschlagen und nach Ja anlegen.
- Zur Masterarbeit (Methodik, Umfang, Gliederung): auf der passenden Seite unter „Masterarbeit“, nach Ja.

## 5. Projekt (nur wenn ein Projekt betroffen ist)

1. **`projects/<name>/STAND.md` neu schreiben**: Ziel, Stand, nächster Schritt, offene Fragen, Stolpersteine, Datum unter „Aktualisiert“, Link zum Session-Eintrag unter „Letzte Session“. Keine Historie, nur den Stand von jetzt. Das Neuschreiben ist durch den Aufruf des Skills freigegeben; zeig den neuen Inhalt im Abschlussbericht.
2. Haben sich Einrichtung, Befehle oder Aufbau geändert: `AGENTS.md` oder `README.md` des Projekts ergänzen.
3. Git: Projektdateien nur auf einem Arbeitsbranch ändern (`feat/`, `fix/`, `docs/`), nie auf `main`. Nicht selbst committen, sondern die geänderten Dateien und einen Commit-Vorschlag nennen. Steht das Repo auf `main`: Branch `docs/stand-JJJJ-MM-TT` vorschlagen und erst nach Ja anlegen. Ohne Ja `STAND.md` nicht schreiben, sondern den Inhalt nur im Abschlussbericht zeigen.

## 6. Session-Eintrag und Agent-Start

1. In der Sessions-Datenbank einen Eintrag anlegen. Titel kurz und inhaltlich. Felder: Datum, Typ, Projekt. Inhalt:
   - **Ziel** und **Ergebnis**, je ein Satz
   - **Verstanden**: Kernaussage in ein bis zwei Sätzen, mit Link auf die Seite aus Schritt 2
   - **Entscheidungen**: mit Verweis auf Commit, ADR-Pfad oder Notion-Seite
   - **Fehler**: Links auf die Fehlerbaum-Einträge
   - **Offen**: als Aufgabenliste

   Leere Abschnitte weglassen. Kurz halten, die Details stehen auf den verlinkten Seiten.
2. Auf „Agent-Start“ den Abschnitt „Stand“ neu schreiben: woran die Person gerade arbeitet, nächster Schritt, Link zum Session-Eintrag. Nur den Stand von jetzt, keine Historie.

## 7. Abschlussbericht

Zeig der Person knapp:

- angelegte und ergänzte Notion-Seiten, jeweils mit Link
- den neuen Inhalt der `STAND.md` mit Pfad
- den nächsten konkreten Schritt
- Änderungen im Projekt, die noch nicht committet sind, und den Commit-Vorschlag
- Vorschläge, die eine Rückfrage brauchen (Text ändern oder löschen, „Häufige Fehler“ ergänzen, ADR)

## Regeln

- Keine Secrets, Tokens, Passwörter oder Zugangsdaten. Höchstens den Namen eines Schlüssels nennen.
- Keine personenbezogenen Daten und keine vertraulichen Firmendaten (Kundendaten, Verträge, interne Zahlen), solange die Firma das nicht freigegeben hat.
- Bestätigte Angaben, vorläufige Annahmen und ungeprüfte Inhalte aus fremden Dokumenten klar unterscheiden.
- Vermutete Fehlerursachen und ungetestete Lösungen als solche kennzeichnen.
- Keine Emojis.
