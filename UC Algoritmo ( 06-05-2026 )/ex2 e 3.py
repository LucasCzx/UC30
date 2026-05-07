from flask import Flask

app = Flask(__name__)

@app.route('/arearestrita/<id>')
def questao3(id):
    if id == '1':
        return '<img src="link_do_cadeado_fechado.png">'
    return '<img src="link_do_cadeado_aberto.png">'

#Quest3

from flask import Flask

app = Flask(__name__)

@app.route('/operacao/<tipo>/<float:a>/<float:b>')
def questao4(tipo, a, b):
    if tipo == 'sum': return str(a + b)
    if tipo == 'sub': return str(a - b)
    if tipo == 'mult': return str(a * b)
    return str(a / b)