def leiaint(msg):
    ok = False
    valor = 0
    global n
    
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro\033[m')
        if ok:
            break
    return valor

# programa principal
n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')