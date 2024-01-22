from flask import Flask, render_template, request

app = Flask(__name__)

gespeicherte_daten = []

@app.route('/')
def startseite():
    return render_template('index.html', daten=gespeicherte_daten)

@app.route('/popup', methods=['GET', 'POST'])
def popup():
    if request.method == 'POST':
        eingabe_daten = request.form['daten']
        gespeicherte_daten.append(eingabe_daten)
        return render_template('popup.html', eingabe_daten=eingabe_daten)
    return render_template('popup.html')

print(gespeicherte_daten)
if __name__ == '__main__':
    app.run(debug=True)
