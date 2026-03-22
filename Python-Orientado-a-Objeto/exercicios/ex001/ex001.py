# Declaração de Classe

class Aluno:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Aluno(a) e tem {self.idade} anos de idade."
    
# Declaração de Objeto
a1 = Aluno()
a1.nome = "Jonathas"
a1.idade = 21
a1.aniversario()
print(a1.mensagem())

a2 = Aluno()
a2.nome = "Mariely"
a2.idade = 27
a2.aniversario()
print(a2.mensagem())