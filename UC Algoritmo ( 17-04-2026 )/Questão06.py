temperaturas = []
for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)
print(f"Média de temperaturas: {media:.2f}")
