
# Flask Webanwendung Dokumentation

## Übersicht
Diese Dokumentation beschreibt die Struktur und Funktionsweise einer Flask-Webanwendung, die Benutzerauthentifizierung, Aufgabenverwaltung und Datenpersistenz mittels SQLite umfasst.

## Konfiguration (app.py)
Die Anwendung wird durch `app = Flask(__name__)` initialisiert und konfiguriert mit:
- `SQLALCHEMY_DATABASE_URI`: Definiert den Pfad zur SQLite-Datenbank (`'sqlite:///eingaben.db'`), wo Benutzer- und Aufgabeninformationen gespeichert sind.
- `SECRET_KEY`: Ein geheimer Schlüssel (`'123456789'`), der für die Sitzungsverwaltung und CSRF-Schutzmechanismen verwendet wird.

## Erweiterungen
- **CSRFProtect**: Schützt die Formulare der Anwendung vor Cross-Site Request Forgery (CSRF) Angriffen.
- **LoginManager**: Verwaltet die Benutzersitzungen und steuert den Zugriff auf routen, die eine Authentifizierung erfordern.

## Datenmodelle (models.py)
- **User**: Stellt einen Anwender mit `username` und `password_hash` dar. Die Klasse `UserMixin` wird für die Integration mit Flask-Login verwendet.
- **Task**: Repräsentiert eine Aufgabe mit `content`, `date`, `person`, `done` Status und einer Beziehung zum Benutzer.

## Benutzerauthentifizierung
- **/login**: Nutzt `request.form` um Benutzerdaten zu erfassen und validiert diese gegen die Datenbank. Bei Erfolg wird der Benutzer eingeloggt und zur Homepage umgeleitet.
- **/logout**: Meldet den aktuellen Benutzer ab und leitet zur Login-Seite um.
- **/register**: Ermöglicht die Registrierung neuer Benutzer, indem ein neuer `User` Datensatz in der Datenbank erstellt wird, nachdem überprüft wurde, dass der Benutzername noch nicht vergeben ist.

## Aufgabenverwaltung
- **/ (Homepage)**: Zeigt eine Liste der Aufgaben des angemeldeten Benutzers an.
- **/popup**: Erlaubt das Erstellen neuer Aufgaben über ein Popup-Formular.
- **/delete_task**: Löscht ausgewählte Aufgaben basierend auf deren IDs.
- **/update_task_status**: Aktualisiert den Erledigungsstatus einer Aufgabe über AJAX-Anfragen.

## Sicherheitsaspekte
- Passwörter werden sicher als Hashes gespeichert, generiert durch `generate_password_hash`.
- CSRF-Schutz wird auf allen Formularen angewendet, um die Sicherheit der Anwendung zu gewährleisten.

## Start der Anwendung
Die Anwendung wird gestartet mit `app.run(debug=True)`, wobei `debug=True` während der Entwicklung gesetzt werden kann, um detaillierte Fehlermeldungen zu erhalten.

## Anmerkungen
- `flash`-Nachrichten werden verwendet, um Feedback an den Benutzer zu kommunizieren (z.B. bei erfolgreicher Registrierung oder Login-Fehlern).
- `db.create_all()` im Anwendungskontext (`app.app_context()`) erstellt die notwendigen Datenbanktabellen basierend auf den definierten Modellen.
