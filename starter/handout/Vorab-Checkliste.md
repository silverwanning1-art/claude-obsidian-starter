# Vorab-Checkliste

Bitte vor dem Workshop erledigen. Die Einrichtung im Workshop dauert nur dann gut eine Stunde, wenn alles hier schon läuft. Für alle Schritte brauchst du keine Admin-Rechte.

Ob alles klappt, prüfst du am Ende mit den Befehlen in der Tabelle „Prüfen“.

## 1. Konto

- [ ] Ein Konto für deinen KI-Assistenten: Claude (mindestens Pro, Anmeldung unter claude.ai) oder ChatGPT mit Codex. Im Workshop arbeiten wir mit Claude Code, Codex geht genauso.

## 2. Programme

| Programm | Wofür | Windows | macOS | Linux |
|---|---|---|---|---|
| Claude Code | der Agent | in PowerShell: `irm https://claude.ai/install.ps1 \| iex` | im Terminal: `curl -fsSL https://claude.ai/install.sh \| bash` | wie macOS |
| Codex (statt Claude Code) | der Agent | in PowerShell: `npm install -g @openai/codex` (braucht Node.js) | im Terminal: `curl -fsSL https://chatgpt.com/codex/install.sh \| sh` oder `npm install -g @openai/codex` | wie macOS |
| Obsidian | dein Vault | Installer von obsidian.md, installiert nur für dich | obsidian.md | Debian, Ubuntu, Mint: `.deb` von obsidian.md, sonst AppImage (nicht Flatpak, siehe Troubleshooting) |
| Git | Coding-Teil | Git for Windows von git-scm.com, „nur für mich“ installieren | im Terminal `git --version`, macOS bietet die Installation dann an | über die Paketverwaltung, z. B. `sudo apt install git` |
| Python 3 | Coding-Teil, Schutz-Hooks | Installer von python.org, Haken bei „py launcher“ | python.org oder Homebrew | meist schon da, sonst Paketverwaltung |

Windows ohne Admin-Rechte: Den Installationsweg für Claude Code (bzw. Codex), Obsidian und Git prüfen wir im Probelauf auf einem Firmen-Laptop. Ist Git installiert, aber `git` wird nicht gefunden, siehe Troubleshooting „Befehl wird nicht gefunden“.

Codex unter macOS und Linux: Empfohlen ist der Installer mit `curl` aus der Tabelle (so steht es auch in der Anleitung von Codex). `npm install -g @openai/codex` braucht unter Linux mit Node.js aus der Paketverwaltung (`apt`) oft `sudo`. Dann lieber den `curl`-Installer nehmen.

## 3. Ordner

- [ ] Einen leeren Ordner `workspace` anlegen, **nicht** in OneDrive, iCloud oder Dropbox.
  - Windows: `C:\Users\<name>\workspace`. Achtung: Auf Firmen-Laptops liegen „Dokumente“ und „Desktop“ oft schon in OneDrive.
  - macOS und Linux: `~/workspace`
- [ ] Den Starter von GitHub als ZIP herunterladen (grüner Knopf „Code“, dann „Download ZIP“) und den **Inhalt** in diesen Ordner entpacken. Im Ordner `workspace` liegen danach direkt `AGENTS.md`, `README.md` und `starter/`.

## 4. Prüfen

Ein neues Terminal öffnen (Windows: PowerShell) und eingeben:

| Befehl | Erwartet |
|---|---|
| `claude --version` (mit Codex: `codex --version`) | eine Versionsnummer |
| `git --version` | `git version …` |
| Windows: `py -3 --version`, sonst `python3 --version` | `Python 3.…` |

Dann einmal `claude` starten und anmelden. Mit Codex: einmal `codex` starten und mit deinem ChatGPT-Konto anmelden. Obsidian einmal öffnen.

Klappt etwas nicht: Notier dir die Fehlermeldung und bring sie mit. Wir lösen es im Workshop vor dem Start.
