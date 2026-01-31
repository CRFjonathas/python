class ContaCliente:
    def __init__(self, numero, IOF, TR, valor_investido, taxa_rendimento):
        self.numero = numero
        self.IOF = IOF
        self.TR = TR
        self.valor_investido = valor_investido
        self.taxa_rendimento = taxa_rendimento

    def calculo_rendimento(self):
        remuneracao = self.valor_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        valorTR = remuneracao * self.TR
        self.valor_investido += remuneracao - valorIOF - valorTR

    def extrato(self):
        print(f"Saldo atual da conta {self.numero} é R$ {self.valor_investido:10,.2f}")