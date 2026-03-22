from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor

        self.mapa_cores = {
            "vermelho": "red",
            "azul": "blue",
            "verde": "green",
            "rosa": "pink",
            "amarelo": "yellow",
            "preto": "black",
            "branco":"white"
        }
        
        self.destampa = False

    def destampar(self):
        self.destampa = True
    
    def escrever(self, msg):
        cor_ingles = self.mapa_cores[self.cor]
        if self.destampa == True:
            print(f"[{cor_ingles}]{msg}[/]", end=" ")
        else:
            print("A caneta está tampada")

    def quebrar_linha(self, linha):
        linha -= 1
        print("\n" * linha)
