valores = []    # lista vazia


while True:     # lop infinito
    valores.append(int(input('Digite um valor: ')))    # recebe um valor e adciona na lista
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':    # se a resposta for igual a N ou n encerra o loop
        break

print('-=' *30)
print(f'Você digitou {len(valores)} valores')
valores.sort(reverse=True)  # Inverte a ordem da lista de crescente para decrescente
print(f'os valores na ordem decrescente {valores}')

if 5 in valores:    # verifica seo valor 5 está incluida na lista
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')