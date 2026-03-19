def verificar_acesso(usuario, senha, tentativas):
    # Regra de bloqueio
    if tentativas >= 3:
        return "Bloqueado"
    
    # Verificação de credenciais
    if usuario == "admin" and senha == "1234":
        return "Acesso total"
    elif usuario == "admin" and senha != "1234":
        return "Senha incorreta"
    else:
        return "Usuário inválido"