velocidade = float(input("Qual é a velocidade atual do carro?"))

if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido que é 80Km/h")
    multa = (velocidade - 80) * 7
    print("Você deve pagar uma multa de R${:.2f!}".format(multa))
print("Tenha um bom dia! Dirija com seguurança!")