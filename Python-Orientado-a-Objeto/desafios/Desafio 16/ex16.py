from classes.Funcionarios import Funcionario
from rich import print

f1 = Funcionario("Jonathas", "TI", "suporte")
f2 = Funcionario("Mariely", "administrativo", "caixa")

print(f1.apresentacao())
print(f2.apresentacao())