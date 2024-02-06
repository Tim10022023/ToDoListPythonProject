
# Dokumentation für app.py

## Konfiguration und Setup
- Die Flask-Anwendung wird initialisiert und konfiguriert, um mit einer SQLite-Datenbank zu arbeiten. CSRF-Schutz und Login-Management werden eingerichtet, um Sicherheit und Benutzerauthentifizierung zu gewährleisten.

## Benutzerauthentifizierung und -management
### Benutzer laden (`load_user`)
- Diese Funktion ist ein Rückruf für Flask-Login, um Benutzerobjekte anhand ihrer ID zu laden. Sie wird verwendet, um den aktuellen Benutzer aus der Session zu ermitteln.

### Login (`/login`)
- **GET-Anfrage**: Zeigt das Login-Formular an.
- **POST-Anfrage**: Verarbeitet die Eingaben des Login-Formulars.
  - Extrahiert `username` und `password` aus dem Formular.
  - Sucht den Benutzer in der Datenbank. Wenn gefunden, wird das Passwort überprüft.
  - Bei erfolgreicher Authentifizierung wird der Benutzer eingeloggt und zur Homepage weitergeleitet. Bei Fehlern wird eine Fehlermeldung angezeigt.

### Logout (`/logout`)
- Der aktuelle Benutzer wird abgemeldet, und die Anwendung leitet zum Login-Formular um.

### Registrierung (`/register`)
- **POST-Anfrage**: Verarbeitet die Eingaben des Registrierungsformulars.
  - Prüft, ob der Benutzername bereits existiert.
  - Erstellt bei Erfolg einen neuen Benutzer mit gehashtem Passwort und speichert ihn in der Datenbank.
  - Leitet nach der Registrierung zum Login-Formular um.

## Aufgabenverwaltung
### Homepage (`/`)
- Listet alle Aufgaben des aktuellen Benutzers auf. Aufgaben können entweder vom Benutzer selbst erstellt oder ihm zugewiesen worden sein.

### Popup zum Hinzufügen von Aufgaben (`/popup`)
- **GET-Anfrage**: Zeigt ein Formular zum Hinzufügen neuer Aufgaben an.
- **POST-Anfrage**: Verarbeitet die Eingaben des Formulars zum Hinzufügen neuer Aufgaben.
  - Extrahiert Aufgabeninhalt, Fälligkeitsdatum und den zugewiesenen Benutzer aus dem Formular.
  - Erstellt eine neue Aufgabe in der Datenbank.
  - Schließt das Popup-Fenster und aktualisiert die Hauptseite.

### Aufgabe löschen (`/delete_task`)
- Empfängt eine Liste von Aufgaben-IDs, die gelöscht werden sollen.
- Löscht jede ausgewählte Aufgabe aus der Datenbank.

### Aufgabenstatus aktualisieren (`/update_task_status/<int:task_id>`)
- Empfängt den neuen Status einer Aufgabe (erledigt/nicht erledigt) als JSON-Daten.
- Aktualisiert den Status der angegebenen Aufgabe in der Datenbank.

## Sicherheit
- Die Anwendung setzt verschiedene Sicherheitsmaßnahmen um, darunter Passwort-Hashing und CSRF-Schutz, um die Datenintegrität und die Sicherheit der Benutzersitzungen zu gewährleisten.

## Datenbankinitialisierung
- Beim Start der Anwendung werden alle erforderlichen Datenbanktabellen basierend auf den Modelldefinitionen erstellt.

## Serverstart
- Der Flask-Server wird gestartet, wobei der Debug-Modus für die Entwicklungsumgebung aktiviert ist.
