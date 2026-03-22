class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e transferencias
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."
    
    def depositar(self, valor):
        if self.saldo < valor:
            return f"Saldo insuficiente"
        else:
            self.saldo += valor
            return f"Deposito bem sucedido"

    def sacar(self, valor):
        if self.saldo < valor:
            return f"Saldo insuficiente"
        else:
            self.saldo -= valor
            return f"Saque bem sucedido"


c1 = ContaBancaria(112, "Jonathas", 3000)
print(c1)