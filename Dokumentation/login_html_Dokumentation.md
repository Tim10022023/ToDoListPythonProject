
# Dokumentation für login.html

## Einleitung
Diese Dokumentation beschreibt detailliert die `login.html`-Seite, die als Anmelde- und Registrierungsformular für eine Webanwendung dient.

## Kopfbereich (`<head>`)
- Legt den Zeichensatz als UTF-8 fest und definiert die Ansichtsfenster-Einstellungen für die responsive Darstellung auf verschiedenen Geräten.
- Bindet CSS-Dateien für das Styling der Seite und spezifischer Elemente wie Buttons und Formulare ein.

## Hauptbereich (`<body>`)
### Anmeldeseite (`#login-page`)
- **Überschrift**: Klärt den Zweck des Abschnitts – Benutzeranmeldung.
- **Anmeldeformular**: Ermöglicht Benutzern, sich mit ihrem Benutzernamen und Passwort anzumelden.
  - **CSRF-Token**: Ein verstecktes Feld, das den CSRF-Token zur Sicherheit der Formularübertragung enthält.
  - **Benutzername**: Ein Textfeld, in das der Benutzer seinen Benutzernamen eingeben muss. Das `required`-Attribut stellt sicher, dass das Feld ausgefüllt wird.
  - **Passwort**: Ein Passwortfeld, das die Eingabe des Benutzerpassworts erwartet, ebenfalls mit dem `required`-Attribut.
  - **Anmeldebutton**: Ein Button, der das Formular zur Authentifizierung an den Server sendet.

### Registrierungsseite (`#register-page`)
- **Überschrift**: Informiert den Benutzer über den Zweck des Abschnitts – neue Benutzerregistrierung.
- **Registrierungsformular**: Ermöglicht es neuen Benutzern, ein Konto zu erstellen.
  - **CSRF-Token**: Schützt das Formular vor CSRF-Angriffen, ähnlich wie im Anmeldeformular.
  - **Benutzername**: Ein Feld für den gewünschten Benutzernamen des neuen Kontos, erforderlich für die Formularübermittlung.
  - **Passwort**: Ein Feld für das Passwort des neuen Kontos, ebenfalls mit dem `required`-Attribut versehen.
  - **Registrierungsbutton**: Ein Button, der das Registrierungsformular zur Erstellung eines neuen Benutzerkontos an den Server sendet.
