resposta = 'S'
soma = quantidade = media = maior = menor = 0

while resposta in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quantidade += 1
    
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continnuar? [S/N] ')).upper().strip()[0]

media = soma / quantidade

print('Você digitou {} numeros e a media foi {}'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
