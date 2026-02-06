from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome 
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, jogo):
        self.jogos_favoritos.append(jogo)

    def ficha(self):
        self.jogos_favoritos.sort(key=str.lower)
        lista_jogos = "\n".join(self.jogos_favoritos)
        cabecalho = f"Nome real: [on blue]{self.nome}[/]\nJogos favoritos:\n"
        texto = f"{cabecalho}[blue]{lista_jogos}[/]"
        painel = Panel(texto, title=f"Jogador <{self.nick}>", width=35)
        print(painel)