
# Flask Webanwendung Dokumentation (mit ChatGPT erstellt)

## Übersicht
Diese Dokumentation bietet einen detaillierten Überblick über die Flask-Webanwendung, einschließlich Konfiguration, Routen, Datenmodellen und Sicherheitsmerkmalen.

## app.py

### Konfigurationen
- **SQLALCHEMY_DATABASE_URI**: Pfad zur Datenbank (`'sqlite:///eingaben.db'`).
- **SECRET_KEY**: Geheimer Schlüssel für die Anwendung (`'123456789'`).

### Erweiterungen
- `CSRFProtect(app)`: Aktiviert den CSRF-Schutz.
- `LoginManager(app)`: Initialisiert den Login-Manager für die Benutzerauthentifizierung.

### Routen
- **/login**: Anmeldeseite für Benutzer.
- **/logout**: Abmelderoute, leitet zur Login-Seite um.
- **/register**: Registrierungsroute für neue Benutzer.
- **/**: Homepage, zeigt Aufgaben des aktuellen Benutzers an.
- **/popup**: Popup zum Hinzufügen neuer Aufgaben.
- **/delete_task**: Route zum Löschen von Aufgaben.
- **/update_task_status/<int:task_id>**: Aktualisiert den Erledigungsstatus einer Aufgabe.

## models.py

### Datenmodelle
- **Task**: Modell für Aufgaben.
- **User**: Benutzerdatenmodell mit Authentifizierungsfunktionen.

### Methoden
- `User.set_password(password)`: Setzt den Passwort-Hash.
- `User.check_password(password)`: Überprüft das Passwort.

## Sicherheit
- Verwendung von `werkzeug.security` für Passwort-Hashing.
- CSRF-Schutz durch `flask_wtf.CSRFProtect`.

## Datenbank
- SQLite als Datenbanksystem.
- `db.create_all()` zum Erstellen der Datenbanktabellen beim Start.

## Anmerkungen
- Nutzung von `flask_login` für Authentifizierung und Sitzungsmanagement.
- Kommunikation von Fehlermeldungen und Bestätigungen über `flash`-Nachrichten.
