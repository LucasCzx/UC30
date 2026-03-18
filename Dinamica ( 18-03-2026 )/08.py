def receber_palavra():
    palavra = str(input("Digite uma palavra: "))
    return len(palavra)

quantidade = receber_palavra()
print(f"A quantidade de letras é {quantidade}")