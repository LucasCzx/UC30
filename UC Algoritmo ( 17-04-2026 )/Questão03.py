# 3. No supermercado, um cliente quer somar o valor de itens até digitar 0. Use while para ler valores (float) e imprimir o total final.
total = 0
while True:
    try:
        valor = float(input("Digite o valor do item (ou 0 para finalizar): "))
        if valor == 0:
            break
        total += valor
    except ValueError:
        print("Entrada inválida. Tem que digitar um número")

print(f"Total final: R$ {total:.2f}")

# Feito com pesquisas na internet, pois não sabia fazer sozinho! Desculpe se ficou feio, mas consegui chegar no resultado final!