from flask import Flask, render_template, request

app = Flask(__name__)

gespeicherte_daten = []
gespeichertes_datum = []

@app.route('/') #rendert/ruft startseite auf
def startseite():
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
