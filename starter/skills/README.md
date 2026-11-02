# Skills

Jeder Ordner hier mit einer `SKILL.md` wird bei der Einrichtung (Schritt 5) kopiert und gilt dann in allen Sessions: unter Claude Code nach `~/.claude/skills/<name>/` (Aufruf `/name`), unter Codex nach `~/.agents/skills/<name>/` (Aufruf `$name`). Das Format der `SKILL.md` ist in beiden Programmen gleich.

Geplant für v1:

| Skill | Wozu | Stand |
|---|---|---|
| `seal-session` | Wissen aus einer Session in Vault und Fehlerbaum übernehmen, `STAND.md` des Projekts neu schreiben | fertig |
| `durchfragen` | vor dem Bauen: Fragen einzeln, jede mit Empfehlung | folgt |
| `erstes-projekt` | geführt vom Ziel bis zum kleinen lauffähigen Tool | folgt |
| `ux-design` | UX erfassen und testen | folgt |

Der Skill `setup` liegt nicht hier, sondern in `.claude/skills/setup/` und als gleiche Kopie für Codex in `.agents/skills/setup/`, weil er nur im Workspace gebraucht wird.
