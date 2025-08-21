from time import sleep


def maior(* num):
    count = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if count == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        count += 1
    print(f'Foram ainformados {count} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    

# Programa princiapal
maior(3, 6, 5, 8, 4)
maior(5, 4, 9)
maior(6, 7 , 9, 5, 7)
maior(0)