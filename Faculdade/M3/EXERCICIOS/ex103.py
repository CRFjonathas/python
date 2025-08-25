def ficha(jogador='<desconhecido>', gols=0):
    return f'O jogador {jogador} fez {gols} gol(s) na temporada'

# programa principal
j = str(input('Nome do joagador: '))
g = str(input('Numero de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if j.strip == '':
    print(ficha(gols=g))
else:
    print(ficha(j,g))