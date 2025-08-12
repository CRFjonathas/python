numeros = list() # cria uma lista vazia

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('valor adcionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'você digitou os valores {numeros}')