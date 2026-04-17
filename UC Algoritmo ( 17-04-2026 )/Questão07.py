vendas = [150.0, 200.5, 300.0, 400.75, 500.0]
total_pares = 0
for valor in vendas:
    if valor % 2 == 0:
        total_pares += valor
print(f"Total de vendas pares: R$ {total_pares:.2f}")
