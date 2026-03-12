def calcularSalario(valor_por_hora, horas_por_dia):
    dias_no_mes = 30
    salario_mensal = valor_por_hora * horas_por_dia * dias_no_mes
    return salario_mensal

valor_por_hora = 20

horas = float(input("Quantas horas você trabalha por dia? "))

salario = calcularSalario(valor_por_hora, horas)

print("Seu salário mensal é: R$", salario)