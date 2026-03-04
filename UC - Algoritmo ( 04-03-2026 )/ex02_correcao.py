numero = int(input("Digite um número: "))

cubo = numero * 3
quadrado = numero * 2

if numero % 2 == 0:
    print(f"Par, este número ao quadrado {quadrado}")
else: 
    print(f"Impar, este número ao cubo é {cubo}")