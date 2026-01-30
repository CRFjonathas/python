from classes.Extrato import Extrato
import datetime

class Conta:
    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
            self.saldo += valor
            self.extrato.transacoes.append(["DEPÓSITO", valor, datetime.datetime.today()])
            return "Deposito bem sucedido.\n"

    def sacar(self, valor):
        if self.saldo < valor:
            return "Saldo insuficiente.\n"
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return "Saque bem sucedido.\n"
        
    def transferir_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return "Saldo insuficiente.\n"
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERÊCIA", valor, datetime.datetime.today()])
            return "Transferência bem sucedida.\n"
        
    def gerar_saldo(self):
        print(f"Conta: {self.numero}\nSaldo: {self.saldo:10.2f}")