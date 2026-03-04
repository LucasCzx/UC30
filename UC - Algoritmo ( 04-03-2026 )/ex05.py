nome = input("Digite seu nome: ")
senha_correta = "123456"

tentativa = 3 

while tentativa > 3:
    senha = input("Digite sua senha: ")

    if senha == senha_correta:
        print(f"Olá, {nome}. Seja bem vindo!")
        break
    
    else:
        tentativa -= 1

        if tentativa == 2:
            print("Senha errada! Você tem 2 tentativas")
        elif tentativa == 1:
            print("Senha errada! Você tem 1 tentativa")
        else:
            print("Senha bloqueada")