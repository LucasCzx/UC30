nome = input("Digite o seu nome completo: ")
if len(nome) > 50:
    print("Seu nome é grande, ele possui mais de 50 caracteres.")
print(f"Ele possui {len(nome)} caracteres.")

valor = int(input("Digite um número: "))
if valor % 2 == 0:
    print("O valor é par")
else:
    print("O valor é impar")

# --------------------------------------------------------

nota = float(input("Digite sua nota: "))
if nota > 10:
    print("Passou")
else:
    if nota == 8:
        print("Atenção")
    else:
        print("Reprovação")

nota = float(input("Digite sua nota: "))

if nota <= 10:
    print("Passou!")
elif nota == 6:
    print("Recuperação")
else:
    print("Reprovado")
# -------------------------------------------------
idade = int(input("Digite sua idade: "))

if idade >= 16 and idade <= 69:
    print("Faixa permitida")
else:
    print("For da faixa")