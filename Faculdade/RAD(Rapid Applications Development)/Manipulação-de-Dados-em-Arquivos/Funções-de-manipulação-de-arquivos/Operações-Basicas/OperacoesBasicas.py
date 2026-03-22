import os

arquivo1 = open("/workspaces/python/Faculdade/RAD(Rapid Applications Development)/Manipulação-de-Dados-em-Arquivos/Funções-de-manipulação-de-arquivos/Operações-Basicas/teste.txt", "w", encoding="utf-8")
print(os.path.abspath(arquivo1.name))

arquivo1.write("Olà, mundo!")

print(arquivo1)
arquivo1.close
