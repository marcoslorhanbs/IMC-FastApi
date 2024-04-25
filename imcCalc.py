def calcular_imc(peso:float, altura:int):
   
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 24.9:
        classificacao = "Peso normal"
    elif imc < 29.9:
        classificacao = "Sobrepeso"
    elif imc < 34.9:
        classificacao = "Obesidade grau 1"
    elif imc < 39.9:
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3"

    return imc

def classificacao_imc(imc):
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 24.9:
        classificacao = "Peso normal"
    elif imc < 29.9:
        classificacao = "Sobrepeso"
    elif imc < 34.9:
        classificacao = "Obesidade grau 1"
    elif imc < 39.9:
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3"
    return classificacao

#imc = calcular_imc()
#print(f"Seu IMC é {imc:.2f} e sua classificação é '{classificacao}'.")
