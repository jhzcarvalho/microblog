from flask import render_template, request, redirect, flash
from app import app


@app.route("/")
@app.route("/index", defaults={"nome": "usuário"})
@app.route("/index/<nome>")
def index(nome):
    return render_template("index.html", nome=nome)


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/autenticar", methods=["POST"])
def autenticar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if usuario == "adm" and senha == "123":
        return f"usuario: {usuario} e senha: {senha}"
    else:
        flash("Dados inválidos")
        return redirect("/login")
