from flask import Flask, render_template, request

app = Flask(__name__)

recados = []

@app.route("/")
def inicio():
    return render_template("index.html", recados=recados)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form["nome"]
    mensagem = request.form["mensagem"]

    recados.append({
        "nome": nome,
        "mensagem": mensagem
    })

    return render_template("index.html", recados=recados)

app.run(debug=True)