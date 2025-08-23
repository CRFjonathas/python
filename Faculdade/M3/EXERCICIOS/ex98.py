from time import sleep                                                                  # IMPORTA UM ESPECIE DE TEMPORIZADOR

def contador(inicio, fim, passo):                                                       # FUNÇÃO CONTADOR COM PARÂMENTROS DE INICIO, FIM E PASSO
    if passo < 0:                                                                       
        passo *= -1                                                                     # SE O VALOR DO PASSO FOR MENOR QUE 0 IRÁ TRANSFORMAR O NUMERO NEGATIVO EM UM NUMERO POSITIVO
    if passo == 0:
        passo = 1                                                                       # SE O PASSO FOR IGUAL A ZERO O VALOR DO PASSO SERÁ IGUAL A 1

    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')                      # IMPRIME OS VALORES DOS PARÂMETROS
    sleep(1.5)                                                                          # FAZ UMA PAUSA NO TERMINAL DE 1,5 SEGUNDOS

    if inicio < fim:                                                                    # CONDIÇÃO PARA AS CONTAGENS NA ORDEM CRESCENTE
        count = inicio                                                                  # CONTADOR RECEBE O VALOR DE PARÂMETRO INICIO
        while count <= fim:                                                             # LAÇO PARA IMPRIMIR A CONTAGEM 
            print(f'{count} ', end='', flush=True)                                      # IMPRIME A SEQUÊNCIA DA CONTAGEM
            sleep(0.5)                                                                  # FAZ UMA PAUSA DE MEIO SEGUNDO ENTRE CADA NUMERO NA CONTAGEM
            count += passo                                                              # O CONTADOR RECEBE O INCREMENTO DE ACORDO COM O VALOR RECEBIDO NO PARÂMETRO PASSO
        print('FIM!')
    else:                                                                               # CONDIÇÃO PARA AS CONTAGENS NA ORDEM DECRESCENTE
        count = inicio                                                                  # CONTADOR RECEBE O VALOR DE PARÂMETRO INICIO
        while count >= fim:                                                             # LAÇO PARA IMPRIMIR A CONTAGEM 
            print(f'{count} ', end='', flush=True)                                      # IMPRIME A SEQUÊNCIA DA CONTAGEM
            sleep(0.5)                                                                  # FAZ UMA PAUSA DE MEIO SEGUNDO ENTRE CADA NUMERO NA CONTAGEM
            count -= passo                                                              # O CONTADOR RECEBE O DECREMENTO DE ACORDO COM O VALOR RECEBIDO NO PARÂMETRO PASSO
        print('FIM!')
    

# PROGRAMA PRINCIPAL

contador(1, 10, 1)                                                                      # CHAMA FUNÇÃO CONTADOR E DECLARA VALORES AOS PARÂMETROS (CONTAGEM NA ORDEM CRESCENTE)
contador(10, 0, 2)                                                                      # CHAMA FUNÇÃO CONTADOR E DECLARA VALORES AOS PARÂMETROS (CONTAGEM NA ORGEM DECRESCENTE)

print('-=' * 30)
print('Personalize a sua contagem:')
i = int(input('Inicio:  '))                                                             # ENTRADA DE DADOS PARA A VARIAVEL i
f = int(input('Fim:     '))                                                             # ENTRADA DE DADOS PARA A VARIAVEL f
p = int(input('Passo:   '))                                                             # ENTRADA DE DADOS PARA A VARIAVEL p

contador(i, f, p)                                                                       # CHAMA A FUNÇÃO CONTADOR E INSERE AS VARIAVEIS i, f e p COMO OS VALORES DOS PARÂMETROS INICIO, FIM E PASSO