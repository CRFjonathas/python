from classes.Funcionario import Funcionario
from rich import print

f1 = Funcionario("Jonathas", "TI", "suporte")
print(f1.apresentacao())

Funcionario.empresa = "Guaibim"

f2 = Funcionario("Mariely", "administrativo", "caixa")
print(f2.apresentacao())