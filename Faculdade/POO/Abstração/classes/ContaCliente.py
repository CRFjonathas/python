from abc import ABC, abstractmethod

class ContaCliente:
    def __init__(self, numero, IOF, TR, valor_investido, taxa_rendimento):
        self.numero = numero
        self.IOF = IOF
        self.TR = TR
        self.valor_investido = valor_investido
        self.taxa_rendimento = taxa_rendimento

    @abstractmethod
    def calculo_rendimento(self):
        pass

    def extrato(self):
        print(f"Saldo atual da conta {self.numero} é R$ {self.valor_investido:10,.2f}")