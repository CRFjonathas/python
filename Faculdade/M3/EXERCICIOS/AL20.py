# FUNÇÃO (exemplo 1)
def linha():
    print('-' * 40)         # a fução é ignorada e so é excutada quando é requisitada dentro do programa principal


# Programa principal
print('EXEMPLO 1:')

linha()                     # moemnto em que a função 'linha()' é requisitada dentro do programa principal
print('CLUBE DE REGATAS DO FLAMENGO')
linha()
print()


# FUNÇÃO (exemplo 2)
def hino(msg):              # cria uma função com um parâmetro (msg) que irá receber um valor quando a função for chamada dentro do programa principal
    print('=' * 50)
    print(msg)


# Programa principal
print('EXEMPLO 2:')

hino('UMA VEZ FLAMENGO...') # o parâmetro (msg) recebe um valor que é inserido dentro dos parenteses da função
hino('...SEMPRE FLAMENGO')
print()


# FUNÇÃO (exemplo 3)
def soma (a, b):
    c = a + b
    print(f'{a} + {b} = {c}')
    print()


# Programa principal 
print('EXEMPLO 3:')
soma(8, 2)
soma(a=4, b=9)
soma(b=2, a=6)
print()


# FUNÇÃO (exemplo 4)
def contador(* num):            # o "*" vai fazer um empacotamento, o parâmetro "num" poderá receber varios valores e nesse caso irá formar uma tupla
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


# Programa principal
print('EXEMPLO 4:')
contador(8, 3, 2)               # tuplas formada pelos valores recebidos no parâmetro "num"
contador(9, 2, 3, 6)
contador(0, 1)
print()


# FUNÇÃO (exemplo 5)
def dobra(lst):
    count = 0
    while count < len(lst):     # laço que que faz com que dobre os valores dentro do parâmetro "lst" que futuramente no programa principal se tornará uma lista
        lst[count] *= 2
        count += 1
        


# Programa principal
print('EXEMPLO 5:')
valores = [2, 4, 6, 8, 10]      # cria uma lista com valores dentro dela
dobra(valores)                  # chama a função em que o parâmetro "lst" receberá o valor de uma lista  -->  "valores"
print(valores)                  # imprime o valor dobrado da lista "valores" depois de ter passado pela função "dobra"