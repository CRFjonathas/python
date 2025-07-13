frase =  str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparce {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A iltima letra A apareceu na posição {}'.format(frase.rfind('A')+1))