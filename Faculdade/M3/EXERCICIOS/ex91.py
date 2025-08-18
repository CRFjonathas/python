from random import randint
from time import sleep
from operator import itemgetter

jogadores ={'jogador1' : randint(1,6),                                              # dicionario recebendo os valores do dado
            'jogador2' : randint(1,6),
            'jogador3' : randint(1,6),
            'jogador4' : randint(1,6)}

ranking = dict()                                                                    # dicionario vazio
print(f'Valores sorteados: ')

for k, v in jogadores.items():                                                      # laço para imprimir joagadpres e valor do dado
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)                # dicionario 'ranking' recebe o valor do dicionario 'jogadores' de forma ordenada

print('-=' *30)
print('     == RANKING ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)