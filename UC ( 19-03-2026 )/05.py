def verificar_acesso(usuario, senha, tentativas):

    if tentativas >= 3:
        return "Bloqueado"
    
    
    if usuario == "admin" and senha == "1234":
        return "Acesso total"
    elif usuario == "admin" and senha != "1234":
        return "Senha incorreta"
    else:
        return "Usuário inválido"