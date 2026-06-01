from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "123"

@app.route('/', methods=['GET', 'POST'])
def inscricao():
    if request.method == 'POST':
        nome = request.form['nome']
        jogo = request.form['jogo']
        email = request.form['email']

        if not nome or not jogo or not email or len(nome) < 4:
            flash('Preencha todos os campos obrigatórios.', 'erro')
        else:
            flash('Inscrição realizada com sucesso!', 'sucesso')

        return redirect(url_for('inscricao'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# Feito com ajuda do ChatGPT