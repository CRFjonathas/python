x = int(input('Digite o primeiro valor: '))
y = int(input('Digitye o segundo valor: '))


if x > y:
    maior = x
    menor = y
    print('Maior numero: {}'.format(maior))
    print('Menor nuemro: {}'.format(menor))
elif y > x:
    maior = y
    menor = x
    print('Maior numero: {}'.format(maior))
    print('Menor nuemro: {}'.format(menor))
else:
    print('Não existe valor maior, os dois são iguais')