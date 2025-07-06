distancia = int(input("Digite a distancia em KM que você percorreu: "))
dias = int(input("Quantidade de dias de aluguel do carro: "))

carro = dias * 60
quilometragem = distancia * 0.15
total  =  carro + quilometragem

print('O preço do aluguel do carro por {} dias custa R${:.2f}, somado a R$0,15 por KM rodados que é igual a R${:.2f}.'.format(dias, carro, quilometragem))
print("TOTAL = R${:.2f}".format(total))