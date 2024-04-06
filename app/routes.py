from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", nome="João")


@app.route("/contato")
def contato():
    return render_template("contato.html")
