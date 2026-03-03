print("Olá, mundo!")
print("Olá, mundo!")
print("Olá, mundo!")
print("Olá, mundo!")

cont = 1

while cont <= 10:
    print("Olá, mundo")
    cont += 1 # cont = cont + 1
print("Fim!")

print(list(range(10)))
print(list(range(1, 10, 2)))

for cont in range(10): # Para cada termo no intervalo de 1 a 10 imprima, "Olá,mundo!"
    print("Olá, mundo!")
print("Fim!")

soma = 0
for termo in range(1, 11):
    soma += termo
print(soma)