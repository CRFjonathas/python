from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')   
    sleep(1.5)

    if inicio < fim:
        count = inicio
        while count <= fim:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count += passo
        print('FIM!')
    else:
        count = inicio
        while count >= fim:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count -= passo
        print('FIM!')
    
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 30)
print('Personalize a sua contagem:')
i = int(input('Inicio:  '))
f = int(input('Fim:     '))
p = int(input('Passo:   '))

contador(i, f, p)

