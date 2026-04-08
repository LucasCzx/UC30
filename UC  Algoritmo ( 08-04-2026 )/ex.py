N = int(input())
R = int(input())
P = int(input())

total_infectados = N
infectados_no_dia = N
dias_passados = 0

if R == 1:
    while total_infectados < P:
        total_infectados += N
        dias_passados += 1
else:
    while total_infectados < P:
        infectados_no_dia *= R
        total_infectados += infectados_no_dia
        dias_passados += 1

print(dias_passados)