Hallo
Wir werden eine To-Do-Liste mit Python-Sellen. Wir planen, einige nette Funktionen wie eine Erinnerung und eine solide solche Funktion aufzunehmen.
Habe Spaß!



# Durchführungskriterien Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erklärt worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studien kennen die Grundelemente der prozeduralen Programmierung. (10)
### Anwendung der Syntax: Deklaration von Funktionen und Routen
```Python
@ app.route ('/ login', Methoden = ['GET','POST'])
def login ():
 # Implementierung der Logik für den Login
```

### If-Modus
```Python
 wenn request.method == 'POST' und current_user.is_authenticated:
 task_content = request.form ["Inhalt"]
 task_date = request.form ["Datum"]
 zugewiesen_to = request.form.get ('zugewiesen_to')
 task_done = 'erledigt' in request.form
       
 new_task = Task (Inhalt = task_content, date = task_date, user_id = zugewiesen_to, zugewiesen_by_id = current_user.id, done = task_done)
 db.session.add (new_task)
 db.session.commit ()
```
### Variablen und Datentypen
```
 task_content = request.form ["Inhalt"]
 task_date = request.form ["Datum"]
 task_done = 'erledigt' in request.form
users = User.query.all ()
```


# Sie können die Syntax und Semantik von Python (10)
### ForSchleifen
```
{% für Aufgabe in Aufgaben%}
    <!-- Anzeige der Task-Details hier -->
{% endfor%}
```
### Einsatz von Bibliotheken
```Python
vom Kolbenimport Kolben, render_template, request, umleiten, url_for, jsonify, blitz
aus flask_wtf CSRFProtect importieren
aus flask_login importieren LoginManager, login_user, logout_user, login_required, current_user
aus werkzeug.security import genere_password_hash, check_password_hash
von Modellen importieren db, Aufgabe, Benutzer
```

# Sie können ein großes Programm selbstverständlich, programmieren und auf Funktionen, die testen (Das Projekt im Team) (10)
[Git Commits!](/Grading/commits.png.)
[Git Commits2!](/ Grading / Commits2.png.)

# Sie kennen verschiedene Datenstrukturen und können diese bestimmte Welle werden. (10)
```Python 
 users = User.query.all ()
 task_content = []
 task_date = []
 task_done = Falsch
 wenn request.method == 'POST' und current_user.is_authenticated:
 task_content = request.form ["Inhalt"]
 task_date = request.form ["Datum"]
 zugewiesen_to = request.form.get ('zugewiesen_to')
 task_done = 'erledigt' in request.form
 new_task = Task (content = task_content, date = task_date, user_id = zugewiesen_to, zugewiesen_by_id = current_user.id, done = task_done)
 db.session.add (new_task)
 db.session.commit () 
```
in diesem Teil des Codes werden die Daten, die im Popup-Fenster eingetrtagen worden sind, gelesen und in der Datenbank wird sie für die Homepage sicher sind.
Natürlich sind wir auch auf den Rest unserer Codes stolz.

## METHODENKOMPETENZ (10 Punkte)

# Die Studien können eine Entwicklungsumgebung werden um Programm zu stellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->
- [GIT](https://github.com/Tim10022023/ToDoListPythonProject)
- VS-Code
- DB-Browser für SQLite




## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studien können ihre Software kennen und verlassen. (5)
Noah: Probleme mit Github -> Branch konnte nicht gemerget werden (erklärt online mit Bildschirm)
Tim: Datenbank konnte nicht geleseen werden -> hat ``db.session.commit()`` gefehlt, Namensgebung in der DB angepasst
Niklas: Im HTML Problem dass die Popup-Seite nicht geschlossen wird wenn auf Save geklickt wird, wurde gelöst durch ``return "<script>window.opener.location.reload(); window.close();</script>"`` in der app.py datei

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
- Flask (flask, flask_login)
- DB (flask_sqlalchemy)
- CSRFProtection (flask_wtf)
- Password-Hash (werkzeug.security)
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->



## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
### Delete User
```python
@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_ids = request.form.getlist('user_ids')
    for user_id in user_ids:
        user = User.query.get_or_404(user_id)
        if user == current_user:
            flash('Sie können sich nicht selbst löschen.')
        else:
            db.session.delete(user)
    db.session.commit()
    return redirect(url_for('homepage'))
```
### Ajax Code:
```
      function updateTaskStatus(checkbox) {
        const taskId = checkbox.getAttribute("data-task-id");
        const doneStatus = checkbox.checked ? 1 : 0;
        const csrfToken = document
          .querySelector('meta[name="csrf-token"]')
          .getAttribute("content");

        var row = checkbox.closest("tr");

        if (checkbox.checked) {
          row.classList.add("task-done");
        } else {
          row.classList.remove("task-done");
        }

        fetch(`/update_task_status/${taskId}`, {
          method: "POST",
          body: JSON.stringify({ done: doneStatus }),
          headers: {
 "Inhaltstyp": "Anwendung / Json",
 "X-CSRFToken": csrfToken,
 },
        }).then((response) => {});
      }
```
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->

Problem: Benutzer können nur Engelgt werden allerdings nicht gelöscht werden
Problem: Kontrollkästchen werden nach neuladen immer wieder hergestellt

## Kenntisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung

# - Datentypen
```Python
Klassenaufgabe (db.Model):
 id = db.Column (db.Integer, primär_key = True)
 content = db.Column (db.String (255), nullable = False)
 done = db.Column (db.Boolean, Standard = False)
```

# - E / A-Operationen und Daceiverarbeitung
```Python
von Modellen importieren db, Aufgabe, Benutzer

task_content = request.form ["Inhalt"]
```


# - Operatoren
```Python
 wenn request.method == 'POST' und current_user.is_authenticated: (z. 71)
 wenn Benutzer und check_password_hash (user.password_hash, Passwort): (z. 26)
 Aufgaben = Task.query.filter ((Task.user_id == current_user.id) | ((Task.assigned_by_id == current_user.id) & (Task.user_id == current_user.id)) .all (z.59)
```
# - Kontrollstrukturen
```Python
für task_id in task_ids:
 task = Task.query.get_or_404 (task_id)
```

# - Funktionen
```Python
@ app.route ('/')
@login_required
def Homepage ():
 Aufgaben = Task.query.filter ((Task.user_id == current_user.id) | ((Task.assigned_by_id == current_user.id) & (Task.user_id == current_user.id)) .all ()
 users = User.query.all ()
 return render_template ('index.html', Aufgaben = Aufgaben, Benutzer = Benutzer)
```

# - Stringverarbeitung

``return redirect (url_for ('homepage'))``


# - Strukturierte Datentype
```Python
Klassenaufgabe (db.Model):
 id = db.Column (db.Integer, primär_key = True, autoincrement = True)
 content = db.Column (db.String (255), nullable = False)
 date = db.Column (db.String (255), nullable = False)
 done = db.Column (db.Boolean, Standard = False)
 user_id = db.Column (db.Integer, db.ForeignKey ('user.id'), nullable = False) 
 zugewiesene_by_id = db.Column (db.Integer, db.ForeignKey ('user.id'), nullable = True) 

 Benutzer = db.relationship ('Benutzer', Foreign_keys = [user_id], backref = db.backref ('tasks', faul = True))
 zugewiesen_by = db.relationship ('Benutzer', Foreign_keys = [zugewiesen_by_id], backref = db.backref ('zugewiesene_tasks', faul = wahr))
```

