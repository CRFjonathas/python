def area(largura, comprimento):
    a = largura * comprimento
    print(f'A area de um terreno {largura}x{comprimento} é de {a}m²')


print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('CUMPRIMENTO (m): '))
area(l, c)