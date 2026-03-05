import random

lista_desafio = [10, 20, 30, 40, 50, 60]

lista_desafio.sort()
print(f"Desafio crescente: {lista_desafio}")

lista_desafio.sort(reverse=True)
print(f"Desafio decrescente: {lista_desafio}")

random.shuffle(lista_desafio)
print(f"Desafio embaralhado: {lista_desafio}")