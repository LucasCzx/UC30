def rank_jogador(pontos, derrotas):

    pontos_finais = pontos - (derrotas * 10)
    

    if pontos_finais < 0:
        return "Banido"
    
 
    if pontos_finais < 100:
        return "Bronze"
    elif pontos_finais < 300:
        return "Prata"
    elif pontos_finais < 600:
        return "Ouro"
    else:
        return "Diamante"