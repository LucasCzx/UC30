from flask import {
    Flask,
    render_template,
    request,
    make_response,
    redirect,
    url_for,

}

app = Flask(__name__)

@app.route('/')
def inicio():

    # Lê o cookie
    tema = request.cookies.get('tema', 'claro')

    return render_template(
        'inicio.html',
        tema=tema
    )

@app.route('/tema/<escolha>')
def trocar_tema(escolha):

    if escolha not in ['claro', 'escuro']:
        escolha = 'claro'

    resposta = make_response(
        redirect(url_for('inicio'))
    )
    
    resposta.set_cookie(
        'tema',
        escolha,
        max_age=60*60*24*30
    )

    return resposta

# Oque é cookie?
Um cookie é um pequeno arquivo de dados que um servidor web armazena no computador do usuário. Ele é enviado de volta ao servidor em cada requisição subsequente, permitindo que o servidor "lembre-se" do estado do usuário, como preferências de tema, itens no carrinho de compras, etc.