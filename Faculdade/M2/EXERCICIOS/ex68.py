from random import randint

count = 0

while True:
    jogador = int(input('Digite um numero: '))  
    pc = randint(0, 10)
    soma = jogador + pc
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ' )).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador escolheu {pc}. Total de {soma}. ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')

    if tipo == 'P':
        if soma %2 == 0:
            print('VOCÊ VENCEU')
            count += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif tipo == 'I':
        if soma %2 == 1:
            print('VOCÊ VENCEU')
            count += 1
        else:
            print('VOCÊ PERDEU')
            break

    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {count} vezes!')