  # DICIONÁRIOS 

pessoas = {'nome' : 'Jonathas', 'sexo' : 'M', 'idade' : '21'}   # Dicionario substitui o valor numerico dos elemento que seriam (0, 1, 2) por nomes como (nome, sexo, idade)

print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')         # imprime o valor dentro dos elementos nome e idade (jonathas, 21) que estâo dentro do dicionario pessoas
print(pessoas.keys())                                           # imprime os elementos (nome, sexo, idade)
print(pessoas.values())                                         # imprime os valores que estão dentro dos elementos
print(pessoas.items())                                          # imprime os elementos e os valores dentro de cada elemento
print()

pessoas['nome'] = 'Nicacio'     # vai alterar o valor do elemento 'nome' = 'Jonathas' por 'Nicacio'
pessoas['peso'] = 64.7          # vai adicionar um novo elemento 'peso' e dar um valor de 64.7

for k in pessoas.keys():
    print(k)                    # imprime os elementos
print()

for v in pessoas.values():
    print(v)                    # imprime os valores
print()

del pessoas['sexo']             # deleta o elemento 'sexo'
for k, v in pessoas.items():
    print(f'{k} = {v}')         # imprime 'elemento = valor'
print()
print()
print()
print()
print()

brasil = []                                             # lista
estado1 = {'uf' : 'Bahia', 'sigla' : 'BA'}              # dicionario 1
estado2 = {'uf' : 'Rio de Janeiro', 'sigla' : 'RJ'}     # dicionario 2
brasil.append(estado1)                                  # adciona o dicionario 1 na lista
brasil.append(estado2)                                  # adciona dicionario 2 na lista

print(estado1)
print(estado2)
print(brasil)                               
print(brasil[0]['uf'])                      # imprime o elemento 'uf' do dicionario que esta dentro do elemento 0 da lista 'brasil'
print(brasil[1]['sigla'])                   # imprime o elemento 'sigla' do dicionario que esta dentro do elemento 1 da lista 'brasil'

estado = dict()             # cria um dicionario
pais = list()               # cria uma lista

for c in range(0,3):
    pais['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    pais.append(estado.copy())                                  # dicionarios não podem fazer fatiamento dos dados, nesse caso se usa o '.copy' para criar fazer uma copia do dicionario para dentro da lista
print(brasil)
print()

for e in brasil:
    print(e)                # imprime os dicionarios 'estado'
print()

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')        # imprime os valores 'uf' e 'sigla' de cada dicionario 'estado'
print()

for e in brasil:
    for v in e.values():
        print(v)                # tambem imprime os valores 'uf' e 'sigla' de cada dicionario 'estado'
