
# Dokumentation für models.py

## Einleitung
Diese Dokumentation bietet eine detaillierte Erläuterung der `models.py`-Datei, die die Datenmodelle für eine Flask-Webanwendung mit Benutzerauthentifizierung und Aufgabenverwaltung definiert.

## Datenbank Setup
- `SQLAlchemy()`: Initialisiert die SQLAlchemy-Instanz, die als ORM (Object Relational Mapper) dient, um die Datenbankoperationen zu vereinfachen.

## Modelle
### Task
Das `Task`-Modell repräsentiert eine Aufgabe in der Anwendung.

- **Attribute**:
  - `id`: Primärschlüssel, automatisch inkrementiert. Eindeutige Identifikation für jede Aufgabe.
  - `content`: Textfeld, das den Inhalt oder die Beschreibung der Aufgabe speichert. Kann nicht leer sein (`nullable=False`).
  - `date`: Speichert das Fälligkeitsdatum der Aufgabe als String. Auch dieses Feld darf nicht leer sein.
  - `done`: Boolesches Feld, das den Status der Aufgabe (erledigt/nicht erledigt) angibt. Standardmäßig ist es `False`.
  - `user_id`: Fremdschlüssel, der auf die `id` des Benutzers verweist, dem die Aufgabe gehört.
  - `assigned_by_id`: Optionaler Fremdschlüssel, der auf die `id` des Benutzers verweist, der die Aufgabe zugewiesen hat.

- **Beziehungen**:
  - `user`: Definiert eine Many-to-One-Beziehung zu `User`. Jede Aufgabe ist genau einem Benutzer zugeordnet, der sie erstellt hat.
  - `assigned_by`: Optional kann eine Aufgabe von einem Benutzer an einen anderen zugewiesen werden. Diese Beziehung ermöglicht es, den Zuweisenden zu identifizieren.

### User
Das `User`-Modell repräsentiert einen Benutzer in der Anwendung und erweitert `UserMixin` für die Authentifizierung.

- **Attribute**:
  - `id`: Primärschlüssel, automatisch inkrementiert. Eindeutige Identifikation für jeden Benutzer.
  - `username`: Eindeutiger Benutzername, der zur Identifikation des Benutzers dient. Kann nicht leer sein.
  - `password_hash`: Speichert das gehashte Passwort des Benutzers. Kann nicht leer sein.

- **Methoden**:
  - `set_password(password)`: Nimmt ein Klartextpasswort entgegen, hasht es und speichert es in `password_hash`.
  - `check_password(password)`: Vergleicht das übergebene Klartextpasswort mit dem gespeicherten Passwort-Hash und gibt `True` zurück, wenn sie übereinstimmen.

## Sicherheitsaspekte
- Das Passwort wird niemals im Klartext gespeichert. Stattdessen wird die `generate_password_hash`-Funktion von Werkzeug verwendet, um das Passwort zu hashen, bevor es in der Datenbank gespeichert wird. Die `check_password_hash`-Funktion ermöglicht es, das Klartextpasswort mit dem gespeicherten Hash zu überprüfen, ohne das tatsächliche Passwort zu kennen.

## Datenbankbeziehungen
- Die Beziehungen zwischen `User` und `Task` ermöglichen es, Aufgaben ihren Erstellern zuzuordnen und optional zu verfolgen, wer eine Aufgabe einem anderen Benutzer zugewiesen hat.
- Rückbeziehungen (`backref`) bieten eine bequeme Möglichkeit, auf die zugehörigen Objekte zuzugreifen. Zum Beispiel kann man über `user.tasks` alle Aufgaben eines Benutzers abfragen.
