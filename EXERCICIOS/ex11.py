altura = float(input('altura: '))
largura = float(input('largura: '))

area = largura * altura
tinta = area / 2

print('Para uma area de {:.2f}M será necessario {:.1f}L de tinta'.format(area, tinta))