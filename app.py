from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Task(db.model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean, default = False)

    def __init__(self, content):
        self.content = content
        self.done = False
    
    def __repr__(self):
        return "<Content %s>" % self.content

db.create_all()

gespeicherte_daten = []
gespeichertes_datum = []

@app.route('/') #rendert/ruft startseite auf
def startseite():
    gespeicherte_daten = Task.query.all()
    return render_template('index.html', daten=gespeicherte_daten)

@app.route('/popup', methods=['GET', 'POST'])
def popup():
    if request.method == 'POST':
        eingabe_daten = request.form['daten']# Extrahiere Daten aus dem Formularfeld 'daten' der POST-Anfrage
        gespeicherte_daten.append(eingabe_daten)# Füge die empfangenen Daten zur Liste 'gespeicherte_daten' hinzu
        eingabe_datum = request.form['date']
        gespeichertes_datum.append(eingabe_datum)
        return render_template('popup.html', eingabe_daten=eingabe_daten, eingabe_datum=eingabe_datum)# Rendere das HTML-Template 'popup.html' und übergebe 'eingabe_daten'
    return render_template('popup.html')# Wenn keine POST-Anfrage vorliegt, rendere einfach das HTML-Template 'popup.html'


if __name__ == '__main__':
    app.run(debug=True)
