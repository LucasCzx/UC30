
def categorizar_imc(peso, altura):
    try:
        peso = float(peso)
        altura = float(altura)
        imc = peso / (altura ** 2)
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"
    except (ValueError, ZeroDivisionError):
        return "Entrada inválida"

# Feito com ajuda de pesquisas na internet, pois não sabia fazer sozinho!