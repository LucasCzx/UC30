from flask import Flask

app = Flask(__name__)

@app.route('/ola/<n>')
def a(n):
    return 'Oi ' + n + ', tudo certo?'

@app.route('/calculo/<int:x>/<int:y>')
def b(x, y):
    r = x + y
    return f'{x}+{y}={r}'

@app.route('/idade/<nome>/<int:i>')
def c(nome, i):
    if i > 17:
        return nome + ' já é adulto'
    return nome + ' ainda não é adulto'

@app.route('/produto/<p>/<float:v>')
def d(p, v):
    return p + ' custa ' + str(round(v, 2))

@app.route('/repetir/<t>/<int:q>')
def e(t, q):
    return (t + ' ') * q

app.run()