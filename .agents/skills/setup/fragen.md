# Fragen für die Einrichtung

Eine Frage pro Nachricht. Jede Frage außer A6 hat einen Vorschlag in Klammern, den die Person mit „ja“ übernimmt. Leite Vorschläge aus früheren Antworten ab, wo es geht (Beispiel: Rolle Vertrieb, also Bereiche Kunden, Angebote, Marketing). Die Kennung in eckigen Klammern ist der Schlüssel in `starter.json`.

## Block A: Grundeinrichtung (Schritt 2)

1. **Wie soll ich dich nennen?** [`name`]
2. **Was machst du beruflich, in einem Satz? Rolle und Firma oder Branche reichen.** [`rolle`]
3. **In welcher Sprache soll ich antworten?** (Deutsch) [`sprache`]
4. **Wie soll dein Vault heißen?** Das ist der Ordner für dein Wissen, den du in Obsidian öffnest. Ein Wort ohne Umlaute, Leerzeichen und Sonderzeichen, Bindestriche gehen. (Wissen) [`vault`]
5. **Welche 3 bis 6 Bereiche hat deine Arbeit?** Jeder Bereich wird ein Unterordner in `10-Arbeit/` im Vault. Mach einen Vorschlag aus Frage 2. [`bereiche`]
6. **Willst du mit deinem KI-Assistenten auch kleine Werkzeuge oder Programme bauen, oder richten wir das später ein?** Ohne Vorschlag, beide Antworten sind gleich gut: jetzt / später. Darfst du in deiner Firma (noch) nicht programmieren, ist „später“ richtig. Bei „später“ lege ich nur einen leeren Ordner `projects/` an, und du brauchst vorerst weder Git noch Python. Nachholen geht jederzeit mit „Einrichtung ergänzen“. [`coding`]
7. Nur bei A6 „jetzt“: **Hast du schon Projekte, für die du mit deinem KI-Assistenten bauen willst? Ein Stichwort pro Projekt reicht, „noch keins“ ist auch gut.** Die Projekte werden nur in die Übersicht eingetragen, Ordner entstehen erst beim ersten Projekt. [`projekte`]
8. Nur bei A6 „jetzt“: **Hast du schon programmiert?** (nein) Antworten: nein / ein bisschen / ja. Davon hängt ab, wie ausführlich ich dir später Code erkläre. [`programmiert`]
9. **Soll ich zwei Beispielnotizen anlegen, damit du siehst, wie Notizen aussehen? Du kannst sie später mit einem Satz löschen lassen.** (ja) [`beispiele`]

## Block B: Kontext (Schritt 7)

Jede Frage darf übersprungen werden („später“). Kurze Antworten reichen, du formulierst sie aus und zeigst sie vor dem Speichern.

| Frage | Datei in `00-Kontext/` |
|---|---|
| 1. Was sollte jemand Neues im Team über dich und deine Arbeit wissen? | `Über mich.md` |
| 2. Für wen arbeitest du? Wer sind deine Kunden oder internen Abnehmer? | `Zielgruppe.md` |
| 3. Was bietet ihr an, und was unterscheidet euch? | `Angebot.md` |
| 4. Wie schreibst du? Gern ein Beispieltext von dir oder drei Wörter, die deinen Stil beschreiben. | `Schreibstil.md` |
| 5. Wie arbeitest du am liebsten mit mir? Kurz oder ausführlich, erst fragen oder gleich machen? | `Arbeitsstil.md` |

## Aktualisierung

Gilt, wenn es schon eine `starter.json` gibt (erneute Einrichtung, auch im zweiten Programm). Antworten veralten, deshalb wird bestätigt statt übernommen.

- **Block A**: Zeig alle gespeicherten Antworten A1 bis A9 als kurze Liste und frag: „Hat sich etwas geändert?“ Frag nur die genannten Punkte neu, eine Frage pro Nachricht, mit der alten Antwort als Vorschlag. Der Rest gilt als bestätigt.
- **Programmieren (A6)**: Steht dort „später“, frag ausdrücklich, ob es jetzt eingerichtet werden soll. Wechselt die Antwort auf „jetzt“, stell A7 und A8 neu. Fehlt `coding` in einer älteren `starter.json`, gilt „jetzt“.
- **Bereiche (A5)**: Neue Bereiche werden neue Unterordner in `10-Arbeit/`. Weggefallene Bereiche werden nie gelöscht. Nenne sie und biete an, sie nach `90-Archiv/` zu verschieben, nur nach Ja.
- **Block B**: Fasse je Datei in `00-Kontext/` in einem Satz zusammen, was drinsteht (oder „noch leer“), und frag, welche aktualisiert werden sollen. Nur diese Fragen stellen. Geänderten Text vor dem Speichern zeigen, bestehenden Text nur nach Ja ersetzen.
- Geänderte Antworten wirken nur auf Text zwischen den Starter-Markern und auf `starter.json`.
