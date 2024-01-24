from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def startseite():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
