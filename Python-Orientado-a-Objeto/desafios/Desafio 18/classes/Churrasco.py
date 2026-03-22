from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):
        consumo = 0.4 * self.quant
        custo = consumo * 82.40
        rateio = custo // self.quant

        painel = Panel(f"Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/] \nCada participante comerá 0.4KG e cada Kg custa R$82.40 \nRecomendo [blue]comprar {consumo:.3f}Kg[/] de carne \nO custo total será de [green]R${custo:.2f}[/]\nCada pessoa pagará [yellow]R${rateio:.2f}[/] para participar.", title=self.titulo, width=80)

        print(painel)