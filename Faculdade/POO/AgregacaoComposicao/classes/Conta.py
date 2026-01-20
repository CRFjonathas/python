from classes.Extrato import Extrato
import datetime


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO -", valor, datetime.datetime.today()])
    
    def sacar(self, valor): # Função retorna VERDADEIRO ou FALSO
        if valor > self.saldo:
            return True     # Saldo insuficiente
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE -", valor, datetime.datetime.today()])
            return False    # Saque bem sucedido
        
    def gerar_saldo(self):
        print(f"\nN° Conta: {self.numero}\nSaldo: R${self.saldo}\n")

    def transfere_valor(self, conta_destino, valor):
        if valor > self.saldo:
            return "Saldo insuficiente."
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERÊNCIA -", valor, datetime.datetime.today()])
            return "Transferência relizada."