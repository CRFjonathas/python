class Extrato:
    def __init__(self):
        self.transacoes = []

    def gerar_extrato(self, conta):
        print(f"Extrato da conta: {conta}")

        for transacao in self.transacoes:
            print(f"{transacao[0]:20s}R$  {transacao[1]:10.2f}      {transacao[2].strftime('%d/%b/%Y')}")