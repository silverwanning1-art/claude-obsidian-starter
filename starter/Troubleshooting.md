# Troubleshooting

Format: Symptom, Ursache, Lösung. Fehlt dein Problem, frag deinen KI-Assistenten und nenn ihm die genaue Fehlermeldung.

## Befehl wird nicht gefunden, obwohl das Programm installiert ist (Windows)

**Symptom:** `git` oder `gh` meldet „wird nicht als Name eines Cmdlet … erkannt“. Mit dem vollen Pfad (`C:\…\Git\cmd\git.exe --version`) funktioniert es.

**Ursache:** Der Installer konnte den Ordner ohne Admin-Rechte nicht in den Suchpfad (`PATH`) des Systems eintragen.

**Lösung:** Den Ordner in den `PATH` deines Benutzers eintragen. Dafür brauchst du keine Admin-Rechte.

1. Startmenü, „Umgebungsvariablen für dieses Konto bearbeiten“ suchen und öffnen.
2. Oben bei den Benutzervariablen `Path` auswählen, „Bearbeiten“, „Neu“.
3. Den Ordner eintragen, in dem `git.exe` liegt. Meist `C:\Users\<name>\AppData\Local\Programs\Git\cmd`. Für `gh` den Ordner mit `gh.exe`.
4. Mit OK schließen, **alle** Terminals schließen und ein neues öffnen.
5. Prüfen: `git --version`.

## Dateien lassen sich nicht schreiben, oder es tauchen Konfliktkopien auf

**Ursache:** Der Workspace liegt in OneDrive, iCloud oder Dropbox.

**Lösung:** Ordner nach `C:\Users\<name>\workspace` (Windows) oder `~/workspace` verschieben, in Claude Code und Obsidian neu öffnen.

## `python3` oder `python` wird unter Windows nicht gefunden

**Ursache:** Unter Windows heißt der Aufruf meist `py`. `python` öffnet sonst eventuell nur den Microsoft Store.

**Lösung:** `py -3 --version` verwenden. Der Starter trägt bei den Hooks automatisch `py` ein.

## Obsidian (Linux, Flatpak) sieht den Workspace nicht

**Ursache:** Das Flatpak darf nur auf freigegebene Ordner zugreifen.

**Lösung:** Obsidian als `.deb` (Debian, Ubuntu, Mint) oder AppImage verwenden oder den Ordner freigeben, zum Beispiel mit Flatseal.

## Obsidian-AppImage startet nicht (Linux)

**Symptom:** Doppelklick auf die AppImage-Datei tut nichts, oder im Terminal steht ein Fehler mit `FUSE` oder `libfuse.so.2`.

**Ursache:** Es fehlt `libfuse2`, ein kleines Systempaket, das AppImages zum Starten brauchen. Neuere Systeme wie Linux Mint 22 und Ubuntu 24.04 bringen es nicht mehr mit.

**Lösung:** Am einfachsten das `.deb`-Paket von obsidian.md nehmen und per Doppelklick installieren. Oder das fehlende Paket nachinstallieren: `sudo apt install libfuse2t64` (Mint 22, Ubuntu 24.04), bei älteren Versionen `sudo apt install libfuse2`.

## Claude befolgt die neuen Regeln nicht

**Ursache:** Die Regeln werden nur beim Start einer Session geladen.

**Lösung:** Session beenden und im Workspace eine neue starten.

## Codex fragt bei der Einrichtung immer wieder nach

**Ursache:** Die Einrichtung schreibt einige Dateien außerhalb des Workspace, etwa in `~/.codex/` (Einstellungen von Codex) und `~/.agents/skills/`. Dafür braucht Codex jedes Mal deine Erlaubnis.

**Lösung:** Das ist gewollt, bitte jeweils zustimmen. Hast du abgelehnt oder lässt Codex das Schreiben gar nicht zu, legt die Einrichtung die fertigen Dateien im Ordner `starter-ausgabe/` in deinem Workspace ab und nennt dir den Befehl, mit dem du sie selbst an die richtige Stelle kopierst.

## Codex kennt meine Regeln im Projektordner nicht

**Symptom:** In einer Session in `projects/<name>/` weiß Codex nichts von deinem Vault oder dem Fehlerbaum.

**Ursache:** Codex liest Regeln nur aus dem Ordner, in dem die Session startet, und aus `~/.codex/AGENTS.md`. Diese Datei fehlt, oder die Session lief schon, bevor die Einrichtung sie angelegt hat.

**Lösung:** Codex im Workspace bitten, die Einrichtung zu ergänzen (sie legt `~/.codex/AGENTS.md` an). Danach die Session beenden und im Projektordner eine neue starten.
