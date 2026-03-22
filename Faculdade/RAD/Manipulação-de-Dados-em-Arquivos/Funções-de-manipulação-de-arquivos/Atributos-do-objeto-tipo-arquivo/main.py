arquivo1 = open("/workspaces/python/Faculdade/RAD/Manipulação-de-Dados-em-Arquivos/Funções-de-manipulação-de-arquivos/Atributos-do-objeto-tipo-arquivo/texto.py")

print("Nome do arquivo: ", arquivo1.name)
print("Modo doo arquivo: ", arquivo1.mode)
print("Arquivo fechado? ", arquivo1.closed)

arquivo1.close()

print("Arquivo fechado? ", arquivo1.closed)