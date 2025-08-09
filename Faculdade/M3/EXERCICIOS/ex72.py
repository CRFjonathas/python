num = ('zero', 'um', 'sois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove','dez', 
        'onze', 'doze', 'treze', 'quatorze','quize', 
        'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')

while True:
    count = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= count <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o numero {num[count]}')