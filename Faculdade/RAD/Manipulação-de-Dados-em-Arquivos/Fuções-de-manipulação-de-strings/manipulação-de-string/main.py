arquivo = open('dados.txt', 'r', encoding='utf-8')

conteudo = arquivo.read()

print("tipo de conteúdo: ", type(conteudo))

print("conteudo retornado pelo read: ")

print(repr(conteudo))

arquivo.close()