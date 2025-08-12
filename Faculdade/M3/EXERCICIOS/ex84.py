grupo = []
pessoas = []
maior = menor = 0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))

    if len(grupo) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    grupo.append(pessoas[:])
    pessoas.clear()
    resposta = str(input("Deseja continuar? [S/N] "))
    
    if resposta in 'Nn':
        break

print('-=' *30)
print(f'Foram cadastradas {len(grupo)} pessoas.')

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == maior:
        print(f'{i[0]}', end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for i in pessoas:
    if i[1] == menor:
        print(f'{i[0]}', end='')
print()