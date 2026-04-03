from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome 
        self.nick = nick
        self.jogos_favoritos = list()

    def add_favoritos(self, jogo):
        self.jogos_favoritos.append(jogo)
        self.jogos_favoritos = sorted(self.jogos_favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [on blue] {self.nome} [/]"
        conteudo += "\nJogos favoritos:"
        for num, jogo in enumerate(self.jogos_favoritos):
            conteudo += f"\n:video_game: [blue]{jogo}[/]"
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(painel)