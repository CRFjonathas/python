tabela = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia',
          'Mirassol', 'Bragantino', 'Botafogo', 'São Paulo',
          'Fluminense', 'Aletico-MG', 'Ceará', 'Corinthians',
          'Internacional', 'Grêmio', 'Santos', 'Vitoria',
          'Vasco da Gama', 'Fortaleza', 'Juventude', 'Sport Recife')

#sorted

print('='*25)
print('TABELA DO BRASILEIRÃO')
print('='*25)
print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print('='*25)
print(f'O 4 ultimos colocados são: {tabela[-4:]}')
print('='*25)
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print('='*25)
print(f'O Flamengo esta na {tabela.index('Flamengo')+ 1}ª posiução')