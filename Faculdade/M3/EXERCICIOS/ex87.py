matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # lista estruturada com 3 linhas e 3 colunas formando uma matriz para receber valores dentros dos '0'

par = maior = col = 0   # variaveis para serem feitos as somas dos pares, soma dos valores da terceira coluna e a soma da segunda linha

for l in range(0,3):    # estrutura de repetição para as LINHAS
    for c in range(0,3):    # estrutura de repetição para as COLUNAS
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))  # receber os valores que vão ser inseridos dentro da lista matriz

print('-=' *30) 
for l in range(0,3):    # estrutura de repetição para as LINHAS
    for c in range(0,3):    # estrutura de repetição para as COLUNAS
        print(f'[ {matriz[l][c]} ]', end='')    # imprime a matriz
        if matriz[l][c] % 2 == 0:   # verifica os valores pares da matriz
            par += matriz[l][c]     # soma os valores pares da matriz
    print()
print('-=' *30)
print(f'A soma dos valores pares é {par}')

for l in range(0,3):    # estrutura de repetição para as LINHAS
    col += matriz[l][2]     # soma os valores da terceira coluna
print(f'A soma dos valores da terceira coluna é {col}')

for c in range(0,3):    # estrutura de repetição para as COLUNAS
    if c == 0:      # verifica se a coluna da matriz é igual a 0 (primeira coluna)
        maior = matriz[1][c]    # 'maior' vai receber o valor da LINHA 1 e COLUNA 0 da matriz
    elif matriz[1][c] > maior:  # verifica se a coluna da matriz é maior que a variavel 'maior' (maior = 0)
        maior = matriz[1][c]    # maior recebe a matriz [1][c] (c = 1 ou c = 2) ---> respectivamente as colunas 2 e 3
print(f'O maior valor da segunda linha é {maior} ')