galera = list()
dado = list()
maior = menor = 0

#print(f'Lista galera: {galera}')
#print(f'Lista dado: {dado}')
#print()

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    #print()
    #print(f'Lista galera: {galera}')
    #print(f'Lista dado: {dado}')
    #print()
    galera.append(dado[:])  # o valor da lista 'dado' é adcionada nadentro da lista 'galera'
    #print(f"Lista 'GALERA' depois de receber o valor da lista 'DADO': {galera}")
    dado.clear()
    #print()
    #print(dado)
    #print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1

print(f'Temos {maior} maiores de idade e {menor} menores de idade.')