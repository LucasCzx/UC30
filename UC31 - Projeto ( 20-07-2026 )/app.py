from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)

arquivo = "livros.json"

if not os.path.exists(arquivo):
    with open(arquivo, "w") as f:
        json.dump([], f)


@app.route("/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        titulo = request.form["titulo"]
        autor = request.form["autor"]
        ano = request.form["ano"]
        categoria = request.form["categoria"]
        quantidade = request.form["quantidade"]

        if titulo == "" or autor == "" or ano == "" or categoria == "" or quantidade == "":
            return render_template("cadastro.html", erro="Preencha todos os campos.")

        if not ano.isdigit():
            return render_template("cadastro.html", erro="Ano inválido.")

        if not quantidade.isdigit() or int(quantidade) <= 0:
            return render_template("cadastro.html", erro="Quantidade inválida.")

        with open(arquivo, "r") as f:
            livros = json.load(f)

        livros.append({
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "categoria": categoria,
            "quantidade": quantidade
        })

        with open(arquivo, "w") as f:
            json.dump(livros, f, indent=4)

        return redirect(url_for("livros"))

    return render_template("cadastro.html")


@app.route("/livros")
def livros():
    with open(arquivo, "r") as f:
        lista = json.load(f)
    return render_template("livros.html", livros=lista)


@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    livro = None

    if request.method == "POST":
        nome = request.form["titulo"].lower()

        with open(arquivo, "r") as f:
            livros = json.load(f)

        for l in livros:
            if l["titulo"].lower() == nome:
                livro = l
                break

    return render_template("buscar.html", livro=livro)


@app.route("/editar/<int:indice>", methods=["GET", "POST"])
def editar(indice):

    with open(arquivo, "r") as f:
        livros = json.load(f)

    if request.method == "POST":
        livros[indice] = {
            "titulo": request.form["titulo"],
            "autor": request.form["autor"],
            "ano": request.form["ano"],
            "categoria": request.form["categoria"],
            "quantidade": request.form["quantidade"]
        }

        with open(arquivo, "w") as f:
            json.dump(livros, f, indent=4)

        return redirect(url_for("livros"))

    return render_template("editar.html", livro=livros[indice])


@app.route("/excluir/<int:indice>")
def excluir(indice):

    with open(arquivo, "r") as f:
        livros = json.load(f)

    livros.pop(indice)

    with open(arquivo, "w") as f:
        json.dump(livros, f, indent=4)

    return redirect(url_for("livros"))


if __name__ == "__main__":
    app.run(debug=True)
    

# Feito com ajuda do chatgpt