N = int(input())
R = int(input())
P = int(input())

infectados = N
novos = N
dias = 0

while infectados < P:
    novos *= R
    infectados += novos
    dias += 1

print(dias)