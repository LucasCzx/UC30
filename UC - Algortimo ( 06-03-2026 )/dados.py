# Quadro de 1 a 10

quadrados = [x**2 for x in range(1,11)]
print("Quadrados: ", quadrados)

# Numeros pares de 1 a 20
pares = [x for x in range(1,21) if x % 2 == 0]
print("Pares: ", pares)

#Vogais de "Programação"
vogais = [letra for letra in "PROGRAMACAO" if letra in "AEIOU"]
print("Vogais: ", vogais)