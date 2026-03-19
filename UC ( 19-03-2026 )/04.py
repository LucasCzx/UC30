def pontuacao_total(pontos, tempo):

    if tempo < 30:
        pontos += 50
    elif tempo > 100:
        pontos -= 20
    
    if pontos > 200:
        return "Recorde"
    
    return pontos