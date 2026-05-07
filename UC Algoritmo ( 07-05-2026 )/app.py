from flask import Flask, render_template

app = Flask(__name__)

# Informações dos gêneros
generos_filmes = {

    "acao": {
        "nome": "Filmes de Ação",
        "imagem": "https://upload.wikimedia.org/wikipedia/pt/thumb/2/2a/TropaDeElitePoster.jpg/250px-TropaDeElitePoster.jpg",
        "descricao": "Os filmes de ação possuem cenas intensas, perseguições, lutas e muita adrenalina."
    },

    "comedia": {
        "nome": "Filmes de Comédia",
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaeDNXDou0AtzEC8cWULC7PdCobV-ojyN4Bw&s",
        "descricao": "Os filmes de cómedia é bom para rir e se divertir, com situações engraçadas e personagens cômicos."
    },

    "terror": {
        "nome": "Filmes de Terror",
        "imagem": "https://upload.wikimedia.org/wikipedia/pt/d/d8/ScaryMovie.jpg",
        "descricao": "Os fimes de terror são para aqueles que gostam de sentir medo, com histórias assustadoras, monstros e suspense."
    }
}

@app.route('/filme/<genero>')

def mostrar_filme(genero):

    genero = genero.lower()

   
    if genero in generos_filmes:

        dados = generos_filmes[genero]

        return render_template(
            'filme.html',
            titulo=dados["nome"],
            imagem=dados["imagem"],
            descricao=dados["descricao"]
        )

   
    else:
        return render_template('erro.html')


if __name__ == '__main__':
    app.run(debug=True)