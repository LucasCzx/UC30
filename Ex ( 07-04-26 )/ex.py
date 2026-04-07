
p = int(input("Qtd P: "))
d = int(input("Qtd D: "))
b = int(input("Qtd B: "))


pontos = (p * 1) + (d * 2) + (b * 3)


if pontos >= 150:
    resultado = "B"
elif pontos >= 120:
    resultado = "D"
elif pontos >= 100:
    resultado = "P"
else:
    resultado = "N"

print(resultado)