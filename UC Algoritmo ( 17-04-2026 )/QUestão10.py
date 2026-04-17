frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contador = 0
for letra in frase:
    if letra in vogais:
        contador += 1
print(f"Número de vogais na frase: {contador}")

# Utilizando a mesma estrutura das outras questões