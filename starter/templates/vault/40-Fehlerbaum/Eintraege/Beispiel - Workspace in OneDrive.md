---
tags: [fehlerbaum, beispiel]
status: beispiel
date: {{DATUM}}
---

# Beispiel - Workspace in OneDrive

> Beispiel-Eintrag aus dem Starter. Löschen mit: „Lösch alle Beispielnotizen aus dem Starter.“

## Symptom

Dein KI-Assistent meldet, dass eine Datei nicht geschrieben werden kann, oder es tauchen Dateien mit dem Zusatz `-Konflikt` oder dem Namen des Laptops auf.

## Ursache

Der Workspace liegt in einem Ordner, den OneDrive synchronisiert. OneDrive sperrt Dateien kurz, während es sie hochlädt, und legt bei gleichzeitigen Änderungen Kopien an.

## Lösung

Workspace nach `C:/Users/<name>/workspace` verschieben, den Ordner in {{AGENT_NAME}} und Obsidian neu öffnen.

## Gelernt

Arbeitsordner für deinen KI-Assistenten gehören nicht in einen synchronisierten Ordner. Sichern geht anders, zum Beispiel über Git.

## Fälle

- {{DATUM}}: Beispiel aus dem Starter, noch kein echter Fall
