from rich import print
from rich.panel import Panel

class Churrasco:
    # Atributos de Classe
    consumo_padrao:float = 0.400
    preco_kg:float = 82.40

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.participantes = quant

    def qtd_carne(self) -> float:
       return self.participantes * Churrasco.consumo_padrao
    
    def custo_total(self) -> float:
        return self.qtd_carne() * Churrasco.preco_kg
    
    def custo_individual(self) -> float:
        return self.custo_total() / self.participantes

    def analisar(self):

        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados[/]"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao:.3f}KG e cada Kg custa R${Churrasco.preco_kg:.2f}"
        conteudo += f"\nRecomendo [blue]comprar {self.qtd_carne():.3f}Kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.custo_total():.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.custo_individual():.2f}[/] para participar."

        painel = Panel(conteudo, title=self.titulo, width=80)

        print(painel)