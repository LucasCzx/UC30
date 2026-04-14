def soma_segura(a, b):
    try:
        return a + b
    except TypeError:
        print("Entrada inválida")
        return 0

a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")

try:
    resultado = soma_segura(float(a), float(b))
except ValueError:
    print("Entrada inválida")
    resultado = 0

print(resultado)