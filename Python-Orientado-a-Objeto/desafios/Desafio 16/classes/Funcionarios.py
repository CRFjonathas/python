class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo"