real = float(input('Digite o valor em reais  que você tem na carteira: '))

dolar = real / 5.42

print('com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))