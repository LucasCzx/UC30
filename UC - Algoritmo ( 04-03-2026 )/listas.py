nome1 = "Paulo"
nome2 = "Caio"
nome3 = "Fabricio"
nome4 = "Lucas"

nomes = ["Caio", "Paulo", "Fabricio", "Lucas"]
print(nomes)

dados = ["Carlos", 0, 1.70, True]
print(dados)
print(type(dados))
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))


lista = ["Cachorro", "Gato"]
print("Original: ", lista)
lista.append("Coelho") #add no fim da lista
print("Atualizado: ", lista)

lista.insert(1, "Grilo") #add na posição determinada
print("Atualizado: ", lista)

lista.extend(["Macaco", "Ovelha"]) #add mais de um dado de uma vez
print("Lista final", lista)

