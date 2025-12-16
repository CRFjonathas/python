valor = float(input('Valor: R$'))

desconto = valor  - ((valor /  100) * 5)

print('Valor com 5% de desconto: R${:.2f}'.format(desconto))