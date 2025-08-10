num = [1, 2, 3, 4, 5, 9] #lista
print('lista')
print(num)

num[5] = 6 #substitui o SEXTO elemento da lista por 6
print('\nsubstitui o SEXTO elemento da lista por 6')
print(num)

num.append(7) #adciona o valor 7 a lista
print('\ndciona o valor 7 a lista')
print(num)

num.sort(reverse=True) #o comando 'sort' ordena na ordem crescente e o 'reverse' iverte a ordem
print('\no comando "sort" ordena na ordem crescente e o "reverse" iverte a ordem')
print(num)

num.insert(5, 0) #inserir o numero 0 na SEXTA posição
print('\ninserir o numero 0 na SEXTA posição')
print(num)

num.pop(5) #deleta o elemento que esta na SEXTA posição (no caso o valor 0 inserido no comando anterior)
print('\ndeleta o elemento que esta na SEXTA posição (no caso o valor 0 inserido no comando anterior)')
print(num)

num.remove(2) #Remove o numero 2 da lista
print('\nRemove o numero 2 da lista')
print(num)

#print(num)