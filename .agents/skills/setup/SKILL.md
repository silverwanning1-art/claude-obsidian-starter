---
name: setup
description: Richtet aus dem Starter das KI-Betriebssystem der Person ein - Vault, projects/, Regeln, Einstellungen von Claude Code oder Codex und Kontext. Nutzen, wenn in AGENTS.md "Einrichtung: offen" steht, wenn die Person "los" schreibt oder die Einrichtung wiederholen, ergänzen oder im zweiten Programm nachholen will.
---

# Einrichtung

Du richtest für eine Person, die meist nicht programmiert, ihren Workspace ein. Sie soll jeden Schritt verstehen. Sprich sie mit „du“ an, schreibe kurz und ohne Fachjargon, erkläre Begriffe beim ersten Auftreten in einem Halbsatz.

Der Workspace ist der Ordner, in dem diese Datei liegt (drei Ebenen über `.claude/skills/setup/` bzw. `.agents/skills/setup/`, beide Kopien sind gleich). Im Folgenden `<workspace>`.

Dieser Skill läuft in Claude Code und in Codex. Abschnitte mit „Nur Claude Code:“ oder „Nur Codex:“ gelten nur im jeweiligen Programm. Erwähne der Person gegenüber nie das andere Programm, seine Dateien oder Begriffe, außer sie fragt danach oder richtet beide ein. Einzige Ausnahme: die Verweisdateien `CLAUDE.md` (Inhalt nur `@AGENTS.md`). Sie stehen in jedem Plan mit dem Zusatz „Verweis auf `AGENTS.md`, damit auch andere KI-Programme dieselben Regeln lesen“. Mehr sagst du dazu nicht.

## Regeln für den ganzen Ablauf

- Keine Skripte. Dateien schreibst du auf dem üblichen Weg deines Programms: Claude Code mit Write und Edit, Codex mit `apply_patch`. Unter Codex sind lesende Shell-Befehle erlaubt (`ls`, `cat`, `Get-Content`). Sonstige Shell-Befehle nur dort, wo ein Schritt es ausdrücklich sagt (Python-Prüfung). So läuft die Einrichtung unter Windows (PowerShell), macOS und Linux gleich.
- Bestehende Dateien nie überschreiben. Ausnahme: die Startdatei `<workspace>/AGENTS.md`, solange sie die Zeile `<!-- starter:bootstrap v1 -->` enthält. Fehlt etwas in einer bestehenden Datei, ergänze es zwischen den Markern `<!-- starter:begin v1 -->` und `<!-- starter:end v1 -->`. Gibt es die Marker schon, ersetze nur den Text dazwischen.
- Groß- und Kleinschreibung unterscheidet keine Dateien: Unter Windows und macOS sind `agents.md` und `AGENTS.md` dieselbe Datei, Anlegen würde sie still überschreiben. Prüfe deshalb vor jedem Anlegen einer Datei oder eines Ordners, ob es den Namen im Zielordner schon in anderer Schreibweise gibt. Dann gilt er als bestehend, und der Plan nennt die vorhandene Schreibweise.
- Bestehende Dateien außerhalb des Workspace (Einstellungen deines Programms) nur mit Vorher-nachher und nach einem Ja ergänzen.
- Pfade in Dateien, JSON und TOML immer mit `/` schreiben, auch unter Windows (`C:/Users/anna/workspace`).
- Keine Secrets erfragen oder speichern (Passwörter, API-Schlüssel, Tokens).
- Halte die Person auf dem Laufenden mit einer Zeile pro Schritt („Schritt 3 von 8: Plan“).

### Vorlagen und Platzhalter

Vorlagen liegen unter `<workspace>/starter/templates/`. Platzhalter sind in Großbuchstaben geschrieben (`{{NAME}}`). Ersetze jeden davon, in allen Dateien, die du kopierst, auch in denen unter `templates/vault/` (zum Beispiel `{{DATUM}}` und `{{AGENT_NAME}}`). Kleingeschriebene wie `{{date}}` in `Templates/` gehören Obsidian und bleiben stehen.

| Platzhalter | Wert |
|---|---|
| `{{NAME}}`, `{{ROLLE}}`, `{{SPRACHE}}`, `{{VAULT}}` | Antworten A1 bis A4 |
| `{{DATUM}}` | heutiges Datum, `JJJJ-MM-TT` |
| `{{WORKSPACE}}` | absoluter Pfad von `<workspace>` mit `/` |
| `{{BEREICHE_ZEILEN}}` | erst die Zeile `` | `10-Arbeit/` | Arbeit, je Bereich ein Unterordner | ``, dann je Bereich `` | `10-Arbeit/<Bereich>/` | <ein Satz> | `` |
| `{{PROJEKTE}}` | Antwort A7 als Liste, bei „noch keins“: `- noch keins` |
| `{{PROGRAMMIEREN}}` | siehe Schritt 4 |
| `{{AGENT_NAME}}` | Claude Code: `Claude`. Codex: `Codex`. Beide eingerichtet: `Claude bzw. Codex` |
| `{{SEAL}}` | samt Backticks. Claude Code: `` `/seal-session` ``. Codex: `` `$seal-session` ``. Beide eingerichtet: `` `/seal-session` (Claude Code) bzw. `$seal-session` (Codex) `` |

„Beide eingerichtet“ heißt: In `starter.json` stehen nach diesem Lauf `claude` und `codex` unter `agents`.

### Wo was liegt

| | Claude Code | Codex |
|---|---|---|
| Einstellungen | `~/.claude/settings.json` | `~/.codex/config.toml`, Verbote in `~/.codex/rules/starter.rules` |
| globale Regeln | (nicht nötig) | `~/.codex/AGENTS.md` |
| Skills | `~/.claude/skills/<name>/`, Aufruf `/name` | `~/.agents/skills/<name>/`, Aufruf `$name` |
| Hooks | `~/.claude/hooks/instruction-files/`, Einträge in `~/.claude/settings.json` | `~/.codex/hooks/instruction-files/`, Einträge in `~/.codex/hooks.json` |

`~` ist der Benutzerordner, unter Windows `C:/Users/<name>`.

## Schritt 1: Vorprüfung

Prüfe still und berichte dann in höchstens fünf Zeilen:

1. **Programm**: Du weißt aus deiner Umgebung, ob du Claude Code oder Codex bist. Merke dir `claude` oder `codex`. Bist du unsicher, frag die Person.
2. **Betriebssystem**: aus deiner Umgebung. Merke dir `windows`, `macos` oder `linux`.
3. **Cloud-Speicher**: Enthält der Pfad von `<workspace>` `OneDrive`, `iCloud`, `Mobile Documents`, `Dropbox` oder `Google Drive`? Dann stopp: Erkläre, dass die Synchronisierung Dateien sperren und Konflikte erzeugen kann, und schlage einen Ort vor (Windows: `C:/Users/<name>/workspace`, macOS und Linux: `~/workspace`). Weiter erst, wenn der Ordner verschoben und neu geöffnet ist oder die Person das Risiko ausdrücklich annimmt.
4. **Frühere Einrichtung**: Gibt es `<workspace>/.claude/starter.json`? Dann lies sie. Ab jetzt läuft die Einrichtung als **Aktualisierung**: Antworten werden bestätigt statt neu erfragt, Vorhandenes wird nur ergänzt. Steht dein Programm noch nicht unter `agents`, sag: „Dein Workspace ist schon eingerichtet. Ich ergänze jetzt die Teile für dieses Programm.“
5. **Bestehender Vault**: Gibt es im Workspace schon einen Ordner mit `.obsidian/`? Dann biete an, diesen als Vault zu nutzen und nur zu ergänzen.
6. **Startdatei**: Steht in `<workspace>/AGENTS.md` die Zeile `<!-- starter:bootstrap v1 -->`? Wenn nicht und es gibt keine `starter.json`, dann hat die Person eigene Regeln. Diese Datei dann nur zwischen Markern ergänzen.

## Schritt 2: Interview

Lies `fragen.md` in diesem Ordner und stelle **Block A**: neu oder, bei einer Aktualisierung, nach dem Abschnitt „Aktualisierung“ dort. Eine Frage pro Nachricht, jede außer A6 mit einem Vorschlag, den die Person mit „ja“ übernehmen kann. Fasse am Ende von Block A die Antworten in einer kurzen Liste zusammen und frag, ob sie stimmen.

Block B (Kontext) kommt erst in Schritt 7.

## Schritt 3: Plan

Zeige den Plan als Baum. Jede Datei bekommt einen Status: `neu`, `existiert, bleibt` oder `wird ergänzt`. Darunter in zwei bis drei Sätzen, was in Schritt 5 an den Einstellungen deines Programms passiert. Beispiel:

```
workspace/
  AGENTS.md                    neu (ersetzt die Startdatei)
  CLAUDE.md                    existiert, bleibt (Verweis auf AGENTS.md, damit auch andere KI-Programme dieselben Regeln lesen)
  projects/                    neu
  Firmenwissen/                neu (Vault)
    AGENTS.md                  neu
    CLAUDE.md                  neu (Verweis auf AGENTS.md, damit auch andere KI-Programme dieselben Regeln lesen)
    00-Kontext/                neu, 5 Dateien
    10-Arbeit/                 neu
      Vertrieb/                neu
    ...
```

Warte auf ein ausdrückliches Ja. Bei Änderungswünschen den Plan anpassen und erneut zeigen.

## Schritt 4: Erzeugen

In dieser Reihenfolge, `V` steht für `<workspace>/<Vault-Name>`:

1. Bei A6 „später“: nur den Ordner `<workspace>/projects/` mit einer leeren `.gitkeep`-Datei. Sonst `<workspace>/projects/README.md` aus `templates/projects-README.template.md`. Die Vorlage `templates/STAND.template.md` brauchst du jetzt nicht, die Regeln aus Punkt 4 verweisen für neue Projekte darauf.
2. Den Vault:
   - `V/AGENTS.md` aus `templates/vault-AGENTS.template.md` (Konventionen für Notizen) und `V/CLAUDE.md` aus `templates/vault-CLAUDE.template.md` (Verweisdatei, siehe Hinweis oben).
   - Gibt es schon eine `V/CLAUDE.md` ohne die Zeile `@AGENTS.md`: stehen lassen und keine `V/AGENTS.md` anlegen. Nur Codex: Sag der Person, dass Codex die Vault-Regeln erst sieht, wenn sie `V/CLAUDE.md` in `V/AGENTS.md` umbenennt und eine neue `V/CLAUDE.md` mit `@AGENTS.md` anlegt.
   - `V/10-Arbeit/` mit einem Unterordner je Bereich, `V/10-Arbeit/<Bereich>/README.md` mit einem Satz, wofür der Bereich da ist.
   - `V/20-Konzepte/`, `V/30-Sessions/`, `V/90-Archiv/`, `V/Attachments/`: leere Ordner bekommen eine `.gitkeep`-Datei ohne Inhalt, damit sie sichtbar bleiben
   - `V/40-Fehlerbaum/Index.md` und `V/40-Fehlerbaum/Eintraege/` aus `templates/vault/40-Fehlerbaum/`
   - `V/Templates/` aus `templates/vault/Templates/`
   - `V/Inbox.md` aus `templates/vault/Inbox.md`
   - Hat die Person in Block A Beispiele gewollt: `templates/vault/20-Konzepte/` und den Beispiel-Eintrag im Fehlerbaum übernehmen. Sonst weglassen und im Index die Beispielzeile streichen.
   - `V/00-Kontext/` aus `templates/vault/00-Kontext/`, zunächst unverändert mit den Leitfragen. Gefüllt wird in Schritt 7.
3. Obsidian-Einstellungen. Gibt es eine Datei nicht, mit diesem Inhalt anlegen. Gibt es sie, nur fehlende Schlüssel ergänzen.
   - `V/.obsidian/app.json`: `{ "attachmentFolderPath": "Attachments", "alwaysUpdateLinks": true }`
   - `V/.obsidian/templates.json`: `{ "folder": "Templates" }`
4. `<workspace>/AGENTS.md` aus `templates/root-AGENTS.template.md`. `{{PROGRAMMIEREN}}` ist die passende Fassung aus `templates/programmieren.template.md`: bei A6 „später“ die Fassung „später“, sonst je nach Antwort A8. Hat die Person eigene Regeln (Schritt 1, Punkt 6), den ganzen Block zwischen den Markern am Ende ihrer Datei ergänzen. `<workspace>/CLAUDE.md` (Verweisdatei) gibt es schon, sie bleibt.
5. `<workspace>/.claude/starter.json` nach dem Muster in `templates/starter.example.json`. Felder, die je Programm gelten (`einstellungen`, `skills`, `hooks`, `global_agents`), haben `claude` bzw. `codex` als Schlüssel. Die Einträge darin setzt du in den Schritten 5 bis 7.

Bei einer Aktualisierung zusätzlich:

- Text zwischen den Markern in `<workspace>/AGENTS.md` und `V/AGENTS.md` mit den aktuellen Antworten neu erzeugen, bei zwei Programmen mit den Werten für „beide eingerichtet“. Text außerhalb der Marker bleibt.
- Wechselt A6 von „später“ auf „jetzt“: `projects/README.md` anlegen (die `.gitkeep` bleibt) und Schritt 6 anbieten, auch wenn dort `später` steht.
- `projects/README.md` hat keine Marker. Nennt sie den Programmnamen oder den Aufruf von `seal-session`, zeig die Stellen und passe sie nur nach Ja an.
- Neue Bereiche bekommen neue Unterordner in `V/10-Arbeit/`. Weggefallene Bereiche nie löschen und nicht ungefragt verschieben. Nenne sie und such vorher im Vault nach Wikilinks auf Notizen darin. Nenne die Notizen, die darauf verweisen, und schlag vor, dass die Person den Ordner in Obsidian nach `V/90-Archiv/` zieht: Obsidian passt die Links dabei selbst an. Will sie, dass du ihn verschiebst: erst kopieren, die Zahl der Dateien in Kopie und Original vergleichen, Links mit Ordnerpfad (`[[10-Arbeit/<Bereich>/…]]`) auf den neuen Pfad ändern und das Original erst nach einem weiteren Ja löschen.
- In `starter.json` dein Programm unter `agents` ergänzen und `aktualisiert` auf das heutige Datum setzen. Alle übrigen Felder bleiben, außer die Person hat Antworten geändert.

Danach: „Öffne jetzt in Obsidian den Ordner `<Vault-Name>` als Vault (Ordner als Vault öffnen) und sag mir, ob du die Ordner siehst.“ Warte auf die Antwort, ehe du weitermachst. Klappt es nicht, siehe `starter/Troubleshooting.md`. Bei einer Aktualisierung mit schon geöffnetem Vault entfällt das.

## Schritt 5: Einstellungen

Diese Dateien gelten für alle Sessions der Person, deshalb besonders vorsichtig.

### Nur Claude Code: `~/.claude/settings.json`

1. Lies sie. Fehlt sie, gilt `{}`.
2. Füge `templates/settings-fragment.json` hinzu: Listen (`additionalDirectories`, `deny`) zusammenführen, ohne Doppelte. Bestehende Einträge nie entfernen oder ändern.
3. Zeige der Person den Unterschied (vorher und nachher, nur die betroffenen Teile) und erkläre jede neue Zeile in einem Halbsatz:
   - `additionalDirectories`: Claude darf aus Projekt-Sessions in den Vault schauen.
   - `deny`-Regeln: Claude darf keine `.env`-Dateien lesen (dort stehen oft Passwörter), keinen Force-Push und kein rekursives Löschen ausführen.
4. Nur nach einem Ja schreiben. Danach die Datei noch einmal lesen und prüfen, ob sie gültiges JSON ist.

Skills: Gibt es `~/.claude/skills/<name>/` schon, überspringe den Skill und sag es („`<name>` ist schon da, bleibt unverändert“). Für die übrigen Ordner unter `<workspace>/starter/skills/`, die eine `SKILL.md` enthalten, frag einmal gesammelt, ob sie nach `~/.claude/skills/<name>/` kopiert werden sollen. Kopiere alle Dateien des Ordners.

In `starter.json`: `einstellungen.claude` (`angelegt`, `ergänzt` oder `übersprungen`), `skills.claude` (Liste).

### Nur Codex: `~/.codex/`

Sag vorher: „Codex fragt gleich mehrmals, ob es außerhalb dieses Ordners schreiben darf. Das ist gewollt, bitte jeweils erlauben.“

1. **`~/.codex/config.toml`** (die Einstellungen von Codex, im Format TOML):
   - Fehlt sie: `templates/codex-config-fragment.toml` mit eingesetztem `{{WORKSPACE}}` schreiben.
   - Gibt es sie: nur fehlende Tabellen und Schlüssel ergänzen. Alle bestehenden Zeilen samt Kommentaren bleiben unverändert und an ihrem Platz. Neue Tabellen kommen ans Ende der Datei. Fehlt `[sandbox_workspace_write]`, den Block aus der Vorlage anhängen. Gibt es die Tabelle, nur `<workspace>` in `writable_roots` ergänzen.
   - `writable_roots` (Ordner, in die Codex schreiben darf) nur ergänzen, wenn `sandbox_mode` fehlt oder `"workspace-write"` ist. Bei anderen Werten nichts ändern und der Person sagen, warum. `sandbox_mode` und `approval_policy` selbst nie ändern.
   - Konflikt (Schlüssel existiert mit anderem Wert): zeigen und fragen, nie still ändern.
   - Vorher-nachher zeigen, jede neue Zeile in einem Halbsatz erklären, nur nach Ja schreiben. Danach neu lesen und als TOML prüfen: jede Tabelle nur einmal, Zeichenketten in Anführungszeichen, alte Zeilen unverändert.
2. **`~/.codex/rules/starter.rules`** (Verbote: kein Force-Push, kein rekursives Löschen) aus `templates/codex-starter.rules`. Gibt es die Datei schon, nicht anfassen und es sagen.
3. **`~/.codex/AGENTS.md`** (Regeln für alle Codex-Sessions) aus `templates/codex-global-AGENTS.template.md`. Gibt es sie, den Block zwischen den Markern am Ende ergänzen bzw. ersetzen, mit Vorher-nachher und Ja. Erkläre: Codex liest Regeln nur aus dem Startordner. Diese Datei sagt Codex in jeder Session, wo Workspace-Regeln und Fehlerbaum liegen.
4. Sag offen: „Codex kennt kein Leseverbot für Dateien. Dass `.env`-Dateien (dort stehen oft Passwörter) nicht gelesen werden, steht nur als Regel in deiner `AGENTS.md`.“
5. **Skills**: Gibt es `~/.agents/skills/<name>/` schon, den Skill überspringen und es sagen („`<name>` ist schon da, bleibt unverändert“). Für die übrigen Ordner unter `<workspace>/starter/skills/` mit einer `SKILL.md` einmal gesammelt fragen, ob sie nach `~/.agents/skills/<name>/` kopiert werden sollen.

Lässt Codex einen Schreibvorgang nicht zu (abgelehnt oder `approval_policy = "never"`): Lege die fertige Datei unter `<workspace>/starter-ausgabe/<Zielname>` ab, nenne den Zielpfad und den Kopierbefehl (Linux und macOS: `mkdir -p` und `cp`, Windows: `New-Item -ItemType Directory -Force` und `Copy-Item`) und mach weiter. Dateien, die als Anweisung gelten, bekommen dort einen anderen Namen (`codex-AGENTS.md`), der Kopierbefehl benennt sie um. Skills und Hook-Skripte nicht ablegen, der Kopierbefehl nimmt sie direkt aus `starter/`. In `starter.json` steht dann `"von Hand kopieren"`.

In `starter.json`: `einstellungen.codex`, `skills.codex`, `global_agents.codex` (`angelegt`, `ergänzt`, `übersprungen` oder `von Hand kopieren`).

## Schritt 6: Schutz vor fremden Anweisungsdateien (optional)

Erkläre in drei Sätzen: Dein Programm liest Dateien wie `AGENTS.md` oder `SKILL.md` automatisch als Anweisung (Claude Code auch `CLAUDE.md`; unter Codex nenne nur `AGENTS.md` und `SKILL.md`). Eine heruntergeladene fremde Datei mit diesem Namen kann es daher steuern. Zwei kleine Programme (Hooks) warnen beim Start und halten an, bevor so eine Datei entsteht.

`H` ist der Hook-Ordner deines Programms (Tabelle oben).

**Programmieren später** (A6): Den Schritt überspringen und sagen: „Diesen Schutz richten wir ein, wenn du mit dem Programmieren anfängst. Er braucht Python, und fremde Anweisungsdateien kommen vor allem mit fremdem Code.“ In `starter.json`: `hooks.<programm>` = `später`. Weiter mit Schritt 7.

**Schon eingerichtet**: Steht in `starter.json` unter `hooks` für dein Programm `eingerichtet`, frag nicht neu und kopiere keine Skripte. Lies nur `H/allowlist.txt` und vergleiche sie mit der Liste aus Punkt 4 unten. Nenne der Person nur die Zeilen, die fehlen; Zeilen, die schon dastehen, nie doppelt eintragen. Nur Claude Code: nach einem Ja selbst ergänzen. Nur Codex: Die Person trägt sie von Hand ein, denn der Hook lehnt das Schreiben in `H/` ab. Fehlt nichts, sag „Der Schutz ist schon eingerichtet“ und mach mit Schritt 7 weiter.

Sonst frag, ob die Person das einrichten will. Wenn ja:

1. Python prüfen. Windows: `py -3 --version`. macOS und Linux: `python3 --version`. Schlägt das fehl, erkläre, dass der Schritt übersprungen wird und später nachgeholt werden kann, und mach mit Schritt 7 weiter.
2. `common.py`, `guard.py` und `scan.py` aus `<workspace>/starter/hooks/instruction-files/` nach `H/` kopieren.
3. `H/config.json` mit `{ "workspace": "<workspace>", "agent": "claude" }` bzw. `"agent": "codex"` anlegen.
4. `H/allowlist.txt` aus `allowlist.example.txt` erzeugen. Darin alle Anweisungsdateien, die die Einrichtung angelegt hat oder die es im Workspace schon gibt, immer als absolute Pfade mit `/` oder `~` wie im Beispiel (relative Pfade erkennt der Hook nicht, dann gilt jede Datei als fremd): `<workspace>/AGENTS.md`, `<workspace>/CLAUDE.md`, `<workspace>/<Vault-Name>/AGENTS.md`, `<workspace>/<Vault-Name>/CLAUDE.md`, `<workspace>/.claude/skills/setup/SKILL.md`, `<workspace>/.agents/skills/setup/SKILL.md`, `<workspace>/starter/skills/<name>/SKILL.md`, dazu `skill:<name>` für jeden Ordner im Skill-Ordner deines Programms. Nur Codex: zusätzlich `~/.codex/AGENTS.md`. Fremde Dateien zeigst du der Person und trägst sie nur nach ihrem Ja ein.
5. Hook-Einträge eintragen, mit Vorher-nachher und Ja wie in Schritt 5:
   - Nur Claude Code: die Einträge aus `starter/hooks/instruction-files/README.md` in `~/.claude/settings.json`. Als Programm unter Windows `py` mit erstem Argument `-3`, sonst `python3`.
   - Nur Codex: die Einträge aus dem Abschnitt „Codex“ in `starter/hooks/instruction-files/README.md` in `~/.codex/hooks.json`, Pfade immer in doppelten Anführungszeichen. Gibt es die Datei, nur die beiden Einträge ergänzen, danach als JSON prüfen. In `~/.codex/config.toml` unter `[features]` `hooks = true` ergänzen (Vorgehen wie in Schritt 5, Konflikt zeigen und fragen).

Sag der Person vorher:

- Nur Claude Code: Beim Schreiben in `~/.claude/hooks/` fragt Claude Code eventuell nach. Das ist gewollt.
- Nur Codex: Codex lässt die Hooks eventuell einmal bestätigen. Statt nachzufragen, lehnt Codex das Anlegen einer solchen Datei ab und erklärt in der Meldung, wie du sie erlaubst.
- Auch beim Anlegen eines neuen Projekts unter `projects/` halten die Hooks an, weil dort Regeldateien entstehen. Das ist erwartet und steht so auch in deinen Regeln. Ich nenne dir dann die zwei Zeilen für `allowlist.txt` (absolute Pfade der neuen `AGENTS.md` und `CLAUDE.md`). Nur Claude Code: Nach deinem Ja in der Rückfrage trage ich sie selbst ein. Nur Codex: Du trägst sie selbst in `~/.codex/hooks/instruction-files/allowlist.txt` ein.

In `starter.json`: `hooks.<programm>` (`eingerichtet`, `übersprungen` oder `von Hand kopieren`).

## Schritt 7: Kontext

Stelle **Block B** aus `fragen.md`, neu oder bei einer Aktualisierung nach dem Abschnitt „Aktualisierung“. Vorher sagen: Diese Antworten landen in `00-Kontext/` und helfen mir, Texte in deinem Sinn zu schreiben. Du kannst jede Frage überspringen und die Dateien später allein ausfüllen. Für Firmendaten gilt: nur, was du auch einer externen Agentur geben würdest.

Schreibe die Antworten in die Dateien unter `V/00-Kontext/`. Bei übersprungenen Fragen bleiben die Leitfragen stehen. Bestehenden Text nur nach Ja ersetzen. Trag das Ergebnis in `starter.json` ein (`kontext`).

## Schritt 8: Prüfen und Abschluss

Prüfe und berichte als Liste mit „ok“ oder dem Problem:

- Alle Dateien aus dem Plan existieren, auch `V/AGENTS.md` (außer im Sonderfall aus Schritt 4).
- In keiner erzeugten Datei steht noch ein Platzhalter in Großbuchstaben (`{{` gefolgt von einem Großbuchstaben).
- Jeder Wikilink in den angelegten Vault-Dateien zeigt auf eine vorhandene Notiz. Wikilinks, die nur das Format zeigen (`[[Wikilinks]]`, `[[Eintrag]]`), zählen nicht.
- Kaltstart: Lies `<workspace>/AGENTS.md` und höchstens zwei Dateien, auf die sie verweist, so als wüsstest du nichts von dieser Einrichtung. Kannst du daraus beantworten, wo der Vault liegt, wo ein neues Projekt beginnt, wo du bei einem Fehler zuerst schaust und wo steht, wer die Person ist? Fehlt eine Antwort, ergänze den Verweis zwischen den Markern der Datei, in die er gehört.
- `starter.json` ist gültiges JSON und nennt dein Programm unter `agents`.
- `<workspace>/AGENTS.md` beginnt nicht mehr mit `<!-- starter:bootstrap v1 -->` und enthält `Einrichtung: abgeschlossen`.
- Nur Claude Code: `~/.claude/settings.json` ist gültiges JSON.
- Nur Codex: `~/.codex/config.toml` ist gültiges TOML, `~/.codex/AGENTS.md` enthält die Marker, `~/.codex/hooks.json` ist gültiges JSON (falls eingerichtet). Abgelegte Dateien unter `starter-ausgabe/` nennst du mit Kopierbefehl noch einmal.

Dann zum Schluss:

1. Eine Liste aller Änderungen, gruppiert nach Workspace, Vault und Einstellungen deines Programms.
2. Der Hinweis: „Beende diese Session und starte eine neue im selben Ordner. Erst dann gelten deine neuen Regeln.“
3. Drei nächste Schritte, angepasst an die Antworten, zum Beispiel: eine Notiz in einem Bereich anlegen lassen, ein erstes Projekt unter `projects/` beginnen, am Ende einer Session `/seal-session` (Claude Code) bzw. `$seal-session` (Codex) ausprobieren. Nenne nur den Aufruf deines Programms. Bei A6 „später“ kein Projekt vorschlagen, sondern sagen, dass sich das Programmieren jederzeit mit „Einrichtung ergänzen“ nachholen lässt.
