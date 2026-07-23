@app.route('/cantinho')
@login_necessario
def cantinho():
    nome = session.get('usuario_nome')

    return render_template(
        'cantinho.html',
        nome=nome,
        cor='Azul',
        linguagem='Python',
        frase='Nunca deixe de aprender.'
    )
