maiores = 0
homens = 0
mulheres20 = 0

while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: [F/M] ')).strip().upper()[0]
    
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade >= 20:
        mulheres20 += 1      
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]    
    if continuar == 'n':
        break
 

print(f'QUANTIDADE DE PESSOAS MAIORES DE 18 ANOS: {maiores}')
print(f'QUANTIDADE DE HOMENS: {homens}')
print(f'QUANTIDADE DE MULHERES MAIORES DE 20 ANOS: {mulheres20}')
