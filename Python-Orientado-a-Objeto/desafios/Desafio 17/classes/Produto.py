from rich.panel import Panel
from rich.text import Text
from rich import print

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        texto = Text(f"{self.nome}\n------------------------------\n..........R${self.preco:,.2f}..........", justify="center")
        painel = Panel(texto, title="Produto", width=35)
        print(painel)