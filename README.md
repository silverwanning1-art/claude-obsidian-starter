# claude-obsidian-starter

Ein Starter, mit dem dein KI-Assistent (Claude Code oder Codex) dir in etwa einer Stunde ein eigenes KI-Betriebssystem einrichtet: einen Obsidian-Vault als Gedächtnis, einen Ordner für Code-Projekte und kurze Regeln, nach denen er mit dir arbeitet. Entstanden für den Workshop „Vibe-Coding im Unternehmen“.

**Start in einem Satz:** Starter als ZIP herunterladen, in einen leeren Ordner außerhalb von OneDrive, iCloud oder Dropbox entpacken, den Ordner in Claude Code oder Codex öffnen und „los“ schreiben.

## 1. Vorbereiten

Die Einrichtung dauert nur dann etwa eine Stunde, wenn diese Schritte vorher erledigt sind. Sie sind so gewählt, dass sie ohne Admin-Rechte gehen sollten.

**Konto:** Claude (mindestens Pro, Anmeldung unter claude.ai) oder ChatGPT mit Codex.

**Programme:**

| Programm | Wofür | Windows | macOS | Linux |
|---|---|---|---|---|
| Claude Code | der Agent | in PowerShell: `irm https://claude.ai/install.ps1 \| iex` | im Terminal: `curl -fsSL https://claude.ai/install.sh \| bash` | wie macOS |
| Codex (statt Claude Code) | der Agent | in PowerShell: `npm install -g @openai/codex` (braucht Node.js) | im Terminal: `curl -fsSL https://chatgpt.com/codex/install.sh \| sh` | wie macOS |
| Obsidian | dein Vault | Installer von obsidian.md, installiert nur für dich | obsidian.md | Debian, Ubuntu, Mint: `.deb` von obsidian.md, sonst AppImage (nicht Flatpak, siehe [Troubleshooting](starter/Troubleshooting.md)) |
| Git | Coding-Teil | Git for Windows von git-scm.com, „nur für mich“ installieren | im Terminal `git --version`, macOS bietet die Installation dann an | über die Paketverwaltung, z. B. `sudo apt install git` |
| Python 3 | Coding-Teil, Schutz-Hooks | Installer von python.org, Haken bei „py launcher“ | python.org oder Homebrew | meist schon da, sonst Paketverwaltung |

Git und Python brauchst du nur, wenn du gleich programmieren willst. Die Einrichtung fragt danach. Sagst du „später“, lässt du die beiden Zeilen weg und holst sie nach, wenn du so weit bist.

Codex unter Linux: `npm install -g @openai/codex` braucht mit Node.js aus der Paketverwaltung oft `sudo`. Dann lieber den `curl`-Installer nehmen.

**Ordner:** Einen leeren Ordner `workspace` anlegen, **nicht** in OneDrive, iCloud oder Dropbox.

- Windows: `C:\Users\<name>\workspace`. Achtung: Auf Firmen-Laptops liegen „Dokumente“ und „Desktop“ oft schon in OneDrive.
- macOS und Linux: `~/workspace`

Dann den Starter als ZIP herunterladen (grüner Knopf „Code“, dann „Download ZIP“) und den **Inhalt** in diesen Ordner entpacken. Im Ordner `workspace` liegen danach direkt `AGENTS.md`, `README.md` und `starter/`.

**Prüfen:** Ein neues Terminal öffnen (Windows: PowerShell) und eingeben:

| Befehl | Erwartet |
|---|---|
| `claude --version` (mit Codex: `codex --version`) | eine Versionsnummer |
| `git --version` (nur fürs Programmieren) | `git version …` |
| Windows: `py -3 --version`, sonst `python3 --version` (nur fürs Programmieren) | `Python 3.…` |

Einmal `claude` bzw. `codex` starten und anmelden, Obsidian einmal öffnen. Klappt etwas nicht, steht die Lösung meist im [Troubleshooting](starter/Troubleshooting.md).

## 2. Einrichten

Im Terminal in den Ordner `workspace` wechseln, `claude` oder `codex` starten und „los“ schreiben. Die Einrichtung:

1. prüft den Ordner (Cloud-Speicher, bestehender Vault, Betriebssystem),
2. stellt dir einzeln ein paar Fragen: Name, Rolle, Bereiche, Projekte,
3. zeigt dir den Plan als Baum und wartet auf dein Ja,
4. legt den Vault, den Ordner `projects/` und die Regeln an,
5. ergänzt mit deiner Zustimmung die Einstellungen von Claude Code oder Codex (Berechtigungen, Skills, optional Schutz-Hooks) und zeigt dir vorher, was sich ändert,
6. füllt zum Schluss mit dir deinen Kontext aus (über dich, Zielgruppe, Angebot, Schreibstil). Das geht auch später allein.

Bestehende Dateien werden nie überschrieben. Die Einrichtung lässt sich wiederholen.

## 3. Danach

- Den Vault-Ordner in Obsidian öffnen („Ordner als Vault öffnen“).
- Session beenden, eine neue starten und fragen: „Was weißt du über mich?“
- Am Ende einer Session, in der du etwas gelernt oder entschieden hast: `/seal-session` (Claude Code) bzw. `$seal-session` (Codex). Das legt das Wichtigste im Vault ab.
- In Claude Code: Für größere Vorhaben den Planmodus nutzen, den Plan in einer Datei speichern und mit `/clear` frisch umsetzen. `/context` zeigt, wie voll das Kontextfenster ist, `/compact` fasst zusammen.

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
| `starter/Troubleshooting.md` | bekannte Probleme und Lösungen |

Entscheidungen zum Aufbau des Starters stehen unter [`docs/adr/`](docs/adr/). Sie sind nicht im ZIP enthalten.

## Lizenz

MIT, siehe [LICENSE](LICENSE).
