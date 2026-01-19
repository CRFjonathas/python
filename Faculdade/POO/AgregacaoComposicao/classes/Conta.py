class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor): # Função retorna VERDADEIRO ou FALSO
        if valor > self.saldo:
            return True     # Saldo insuficiente
        else:
            self.saldo -= valor
            return False    # Saque bem sucedido
        
    def gerar_saldo(self):
        print(f"N° Conta: {self.numero}\nSaldo: R${self.saldo}")

    def transferencia(self, contaDestino, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente.")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ("Transferência relizada.")