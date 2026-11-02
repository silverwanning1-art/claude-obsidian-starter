<!-- starter:begin v1 -->
# Workspace von {{NAME}}

Der Workspace (Arbeitsordner mit Vault, Projekten und Regeln) liegt unter `{{WORKSPACE}}`.

Diese Datei lädt Codex in jeder Session auf diesem Rechner. Die folgenden Regeln gelten nur, wenn der Startordner der Session unter `{{WORKSPACE}}` liegt. Für Sessions außerhalb von `{{WORKSPACE}}` gilt dieser Abschnitt nicht.

- Liegt der Startordner unter `{{WORKSPACE}}`, aber nicht direkt darin (z. B. `projects/<name>/` oder der Vault): zuerst `{{WORKSPACE}}/AGENTS.md` lesen und befolgen. Codex lädt Regeln aus übergeordneten Ordnern nicht von selbst.
- Bei Fehlern zuerst `{{WORKSPACE}}/{{VAULT}}/40-Fehlerbaum/Index.md` lesen.
- Skills werden mit `$name` aufgerufen, zum Beispiel `$seal-session`.
<!-- starter:end v1 -->
