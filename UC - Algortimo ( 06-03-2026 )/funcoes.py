notas = [7.5, 8.0, 9.5, 6.0, 8.5]

print("Notas: ",notas)

print("Menor: ", min(notas))

print("Maior: ", max(notas))
print("Soma: ", sum(notas))
print("Média: ", sum(notas) / len (notas))

nomes = ["Adriana" , "Breno", "Carla", "Daniel"]

# Apenas o elemento
print("Usando FOR simples: ")
for nome in nomes:
    print(f"Olá {nome}!")

# Indice e elemento
print("\n Usando enumerante: ")
for indice, nome in enumerate(nomes):
    print(f"Posição {indice}: {nome}")

original = ["A", "B", "C"]
copia = list(original)

print("Orginal: ", original)
print("Cópia: ", copia)
print("São iguais: ", original == copia)

copia.append("D")
print("Original", original)
print("Cópia: ", copia)
print("São iguais: ", original == copia)