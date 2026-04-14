def divisao(x, y):
    try:
        return float(x) / float(y)
    except ZeroDivisionError:
        return "Não divida por zero!"
    except (TypeError, ValueError):
        return "Entrada inválida"

x = input("Digite o primeiro número: ")
y = input("Digite o segundo número: ")

print(divisao(x, y))