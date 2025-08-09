# TUPLAS

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche: # não é possivel mostrar posição
    print(f'Eu vou comer {comida}')

for count in range(0, len(lanche)): # estrutura faz com que seja possivel mostrar a posição
    print(f'Eu vou comer {lanche[count]} na posição {count}')

for pos, comida in enumerate(lanche): # tambem mostra posição
    print(f'Eu vou comer {comida} na posição {pos}')