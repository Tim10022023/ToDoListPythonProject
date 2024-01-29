from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eingaben.db'
db = SQLAlchemy(app)

class Eingabe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    daten = db.Column(db.String(255), nullable=False)
    datum = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)

@app.route('/')
def startseite():
    eingaben = Eingabe.query.all()
    return render_template('index.html', eingaben=eingaben)

@app.route('/popup', methods=['POST','GET'])
def popup():
    eingabe_daten=[]
    eingabe_datum=""
    eingabe_name=""
    if request.method == 'POST':
        eingabe_daten = request.form["daten"]
        eingabe_datum = request.form["date"]
        eingabe_name = request.form["name"]

        neue_eingabe = Eingabe(daten=eingabe_daten, datum=eingabe_datum, name=eingabe_name,)
        db.session.add(neue_eingabe)
        db.session.commit()

    return render_template('popup.html', eingabe_daten=eingabe_daten, eingabe_datum=eingabe_datum,)



@app.route('/loesche_eingaben', methods=['POST'])
def loesche_eingaben():
    eingabe_ids = request.form.getlist('eingabe_ids')
    for eingabe_id in eingabe_ids:
        eingabe = Eingabe.query.get_or_404(eingabe_id)
        db.session.delete(eingabe)
    db.session.commit()
    return redirect(url_for('startseite'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #wird benötigt damit man vom lokalen Netz zugreifen kann
    with app.app_context():
        db.create_all()
    app.run(debug=True)
