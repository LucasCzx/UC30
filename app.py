from flask import Flask, render_template

app = Flask(__name__)

cardapio = [
    {'id': 1, 'nome': 'X-Burguer', 'preco': 15.00},
    {'id': 2, 'nome': 'X-Salada', 'preco': 18.00},
    {'id': 3, 'nome': 'Bacon Egg', 'preco': 20.00},
    {'id': 4, 'nome': 'Batata Frita', 'preco': 10.00},
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
   
    return render_template('cardapio.html', lanches=cardapio)

@app.route('/lanche/<int:lanche_id>')
def lanche(lanche_id):
 
    lanche_encontrado = None
    for lanche in cardapio:
        if lanche['id'] == lanche_id:
            lanche_encontrado = lanche
            break
    
   
    if lanche_encontrado is None:
        return "<h1>Num achei teu lanche não, visse?</h1><a href='/cardapio'>Voltar</a>", 404
    
   
    return render_template('lanche.html', lanche=lanche_encontrado)


if __name__ == '__main__':
    app.run(debug=True)