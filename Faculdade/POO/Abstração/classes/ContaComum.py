from classes.ContaCliente import ContaCliente

class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, TR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, TR, valor_investido, taxa_rendimento)

    def calculo_rendimento(self):
        remuneracao = self.valor_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        self.valor_investido += remuneracao - valorIOF