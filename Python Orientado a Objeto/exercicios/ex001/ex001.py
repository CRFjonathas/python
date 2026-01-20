# Declaração de Classe

class Jogador:
    def __init__(self):     # Metodo Contrutor
        # Atributos de Instancia
        self.nome = ""
        self.gol = 0

    # Metodos de Instancia
    def artilheiro(self):
        self.gol += 1

    def mensagem(self):
        return f"O jogador {self.nome} tem {self.gol} gols na artilharia do campeonato."


# Declaração de Objeto

j1 = Jogador()
j1.nome = "Bruno Henrique"
j1.gol = 16
print(j1.mensagem())

j2 = Jogador()
j2.nome = "Arrascaeta"
j2.gol = 10
j2.artilheiro()
print(j2.mensagem())
