from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Guarda os dados do usuario
nome_usuario = ""
senha_usuario = ""


@app.route("/", methods=["GET", "POST"])
def cadastro():
    global nome_usuario, senha_usuario

    if request.method == "POST":
        nome_usuario = request.form["nome"]
        senha = request.form["senha"]

        # Cria o hash da senha
        senha_usuario = generate_password_hash(senha)

        return redirect(url_for("login"))

    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    mensagem = ""

    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]

        if nome != nome_usuario:
            mensagem = "Usuário não encontrado."

        elif check_password_hash(senha_usuario, senha):
            return redirect(url_for("inicio"))

        else:
            mensagem = "Senha inválida."

    return render_template("login.html", mensagem=mensagem)


@app.route("/inicio")
def inicio():
    return render_template("inicio.html", nome=nome_usuario)


app.run(debug=True)