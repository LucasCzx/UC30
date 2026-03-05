import random

numeros = [91, 34, 67, 15, 82]
print(f"Lista original: {numeros}")

numeros.sort()
print(f"Ordem crescente: {numeros}")

numeros.sort(reverse=True)
print(f"Ordem decrescente: {numeros}")

numeros3 = [6, 7, 8, 9, 10]
random.shuffle(numeros3)
print(f"Lista embaralhada: {numeros3}")