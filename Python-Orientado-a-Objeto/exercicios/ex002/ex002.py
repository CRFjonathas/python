# Declaração de Classe

class Aluno:
    def __init__(self, nome = "vazio", idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é Aluno(a) e tem {self.idade} anos de idade."
    
# Declaração de Objeto
a1 = Aluno("Jonathas", 21)
a1.aniversario()
print(a1)

a2 = Aluno("Mariely", 27)
a2.aniversario()
print(a2)

a3 = Aluno()
print(a3)