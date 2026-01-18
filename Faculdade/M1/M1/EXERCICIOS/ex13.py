salario = float(input('Salario: R$'))

aumento = salario  + ((salario /  100) * 15)

print('Novo salario: R${:.2f}'.format(aumento))