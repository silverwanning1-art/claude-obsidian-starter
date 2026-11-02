# Abschnitt „Programmieren“ für die Root-AGENTS.md

Der Skill `setup` übernimmt genau eine Fassung, ohne Überschrift, je nach Antwort A7.

## Fassung „nein“ und „ein bisschen“

- Vor dem Bauen erklären, was entsteht, und auf ein Ja warten. Fachbegriffe beim ersten Auftreten in einem Halbsatz erklären.
- Klein anfangen: erst eine lauffähige einfache Version, dann erweitern. Nach jedem Schritt sagen, wie {{NAME}} das Ergebnis selbst ausprobiert.
- Jedes Projekt ist ein eigenes Git-Repo. Änderungen in kleinen Commits mit kurzer Beschreibung, was und warum.
- Nichts veröffentlichen, hochladen oder deployen ohne ausdrückliche Freigabe.
- Keine Konten anlegen und keine Programme installieren, ohne vorher zu fragen.

## Fassung „ja“

- In Projekt-Repos nicht direkt auf `main` arbeiten. Branches: `feat/`, `fix/`, `docs/`.
- Kleine, abgeschlossene Commits: `typ: beschreibung` (feat, fix, docs, test, refactor, chore).
- Vor dem Commit Tests und Linter laufen lassen, soweit das Projekt sie hat.
- Merge und Deploy nur nach Freigabe durch {{NAME}}.
- Entscheidungen mit Tragweite als kurze Notiz unter `docs/adr/` im Projekt.
