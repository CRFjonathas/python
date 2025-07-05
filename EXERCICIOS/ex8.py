medida = float(input("Digite uma distancia em metros: "))

cm = medida * 100
mm = medida * 1000

print('Amedai de {:.0f}M é {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))