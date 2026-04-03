from rich.panel import Panel
from rich import print

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        texto = f"{self.nome.center(30, ' ')}"
        texto += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        texto += f"{precof.center(30, '.')}"
        painel = Panel(texto, title="Produto", width=34)
        print(painel)