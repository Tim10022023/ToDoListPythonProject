
# Dokumentation für index.html

## Einleitung
Diese Dokumentation erläutert detailliert das HTML-Snippet einer To-Do-Liste-Seite, einschließlich der Struktur, der eingebetteten Logik und der interaktiven Elemente.

## Kopfbereich (`<head>`)
- Definiert Metadaten wie CSRF-Token, Zeichensatz und Ansichtsfenster-Einstellungen für die responsive Darstellung.
- Bindet externe CSS-Dateien für das Styling der Seite und spezifische Elemente wie Buttons ein.
- Verweist auf ein Favicon, das in der Browser-Tab-Leiste angezeigt wird.

## Hauptbereich (`<body>`)
### Überschrift
- Zeigt den Titel der To-Do-Liste an, der die Namen der Ersteller enthält.

### Button-Bereich
- Enthält Buttons für das Hinzufügen neuer Aufgaben und zum Löschen ausgewählter Aufgaben.
- Der Logout-Button ermöglicht es dem Benutzer, sich sicher abzumelden.

### Löschen-Formular (`<form id="deleteForm">`)
- Beinhaltet eine Tabelle, die alle Aufgaben des Benutzers auflistet, mit Optionen zum Markieren als erledigt und zum Auswählen für das Löschen.
- Jede Aufgabe wird in einer eigenen Tabellenzeile dargestellt, mit Details wie Inhalt, Fälligkeitsdatum und dem Ersteller der Aufgabe.
- Erledigte Aufgaben werden visuell hervorgehoben, basierend auf ihrer `done`-Eigenschaft.

## JavaScript-Funktionalitäten
### Aufgabenstatus aktualisieren (`updateTaskStatus`)
- Wird aufgerufen, wenn der Benutzer den Erledigt-Status einer Aufgabe ändert.
- Sendet eine AJAX-Anfrage an den Server, um den Status in der Datenbank zu aktualisieren.
- Passt das Aussehen der Aufgabe in der Liste basierend auf ihrem Status an.

### Neues Aufgaben-Popup (`oeffnePopup`)
- Öffnet ein neues Fenster mit dem Formular zum Hinzufügen einer neuen Aufgabe, wenn der Benutzer auf den "New Item"-Button klickt.

## Sicherheitsaspekte
- Nutzt ein CSRF-Token in Formularen, um die Sicherheit von Formularübertragungen zu gewährleisten und CSRF-Angriffe zu verhindern.

## Styling und Layout
- Verwendet CSS-Klassen und Inline-Styling, um das Erscheinungsbild der Seite und ihrer Elemente, wie Buttons und Tabellen, zu definieren.

## Interaktivität und Benutzererfahrung
- Bietet interaktive Elemente wie Buttons und Checkboxen, die es dem Benutzer ermöglichen, Aufgaben effektiv zu verwalten.
- Nutzt JavaScript und jQuery für dynamische Inhaltsaktualisierungen und verbesserte Interaktivität ohne Seitenneuladung.
