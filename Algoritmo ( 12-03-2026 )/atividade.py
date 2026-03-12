numero = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

def numeros(numero, numero2):
    soma = numero + numero2
    multiplicacao = numero * numero2
    return soma, multiplicacao

resultado = numeros(numero, numero2)
print(f"A soma e o produto é igual a {resultado}")