
# Dokumentation für popup.html

## Einleitung
Diese Dokumentation beschreibt detailliert die `popup.html`-Seite, die als interaktives Formular zur Eingabe neuer Aufgaben in einer To-Do-Liste-Webanwendung dient.

## Kopfbereich (`<head>`)
- Definiert wichtige Metadaten wie den CSRF-Token für die Formularsicherheit, den Zeichensatz und die Ansichtsfenster-Einstellungen für die responsive Gestaltung.
- Bindet CSS-Dateien ein, um das Erscheinungsbild des Popups und seiner Elemente zu stylen.

## Hauptbereich (`<body>`)
### Überschrift
- Zeigt den Titel der Popup-Seite an, der den Zweck des Popups klarstellt.

### Aufgabenformular (`<form>`)
- **Aufgabeninhalt (`<input type="text" id="content" name="content">`)**: Ermöglicht dem Benutzer, die Beschreibung der neuen Aufgabe einzugeben. Das `required`-Attribut stellt sicher, dass der Benutzer dieses Feld ausfüllen muss.
- **Datum (`<input type="date" id="date" name="date">`)**: Ermöglicht dem Benutzer, ein Fälligkeitsdatum für die Aufgabe auszuwählen.
- **Person zuweisen (`<select name="assigned_to" id="assigned_to">`)**: Ein Dropdown-Menü, das eine Liste aller Benutzer anzeigt, denen die Aufgabe zugewiesen werden kann. Die Optionen werden dynamisch aus der Benutzerdatenbank generiert.
- **Speichern-Button (`<button id="save" type="submit">`)**: Speichert die neue Aufgabe, wenn der Benutzer auf diesen Button klickt. Die Daten werden an den Server gesendet, indem das Formular an die `popup`-Route übermittelt wird.
- **Abbrechen-Button (`<button id="cancel" type="button">`)**: Ermöglicht es dem Benutzer, das Popup zu schließen, ohne eine Aufgabe hinzuzufügen. Die `closeWindow`-Funktion wird durch das `onclick`-Ereignis aufgerufen.

## JavaScript-Funktionalitäten
- **`closeWindow()`**: Eine JavaScript-Funktion, die das Popup-Fenster schließt. Diese Funktion wird aufgerufen, wenn der Benutzer auf den Abbrechen-Button klickt, was eine benutzerfreundliche Möglichkeit bietet, den Vorgang abzubrechen.

## Sicherheitsaspekte
- Das Formular enthält ein verstecktes Feld, das den CSRF-Token übermittelt, um die Sicherheit der Formularübertragung zu gewährleisten und CSRF-Angriffe zu verhindern.

## Styling und Layout
- Das Aussehen des Popups und seiner Elemente wird durch die eingebundenen CSS-Dateien definiert, die ein konsistentes und ansprechendes Design gewährleisten.

