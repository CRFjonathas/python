# CRIAÇAO DA CLASSE
class Conta:
    # MÉTODO CONSTRUTOR
    def __init__(self, numero, nomeTitular, cpf, saldo):
        # ATRIBUTOS:
        self.numero = numero
        self.nomeTitular = nomeTitular
        self.cpf = cpf
        self.saldo = saldo

    # MÉTODO:
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor): # Função retorna VERDADEIRO ou FALSO
        if valor > self.saldo:
            return True     # Saldo insuficiente
        else:
            self.saldo -= valor
            return False    # Saque bem sucedido
        
    def gerar_extrato(self):
        print(f"N° Conta: {self.numero}\nNome do Titular: {self.nomeTitular}\nCPF: {self.cpf}\nSaldo: R${self.saldo}")

    def transferencia(self, contaDestino, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente.")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ("Transferência relizada.")
        
# CODIGO PRINCIPAL:

c1 = Conta(1, "Jonathas", 9707602562, 2300)
c2 = Conta(2, "Maria Cecilia", 7373792359, 25000)
c1.gerar_extrato()
c2.gerar_extrato()
c1.depositar(700)
valor_saque = 1000
resultado_saque = c1.sacar(valor_saque) # Verifica o resultado da função se é VERDADEIRO ou FALSO

if resultado_saque:
    print(f"Saque de R${valor_saque} realizado com sucesso.")
else:
    print(f"Saldo insuficiente.")

c1.gerar_extrato()

c1.transferencia(c2, 1300)

c1.gerar_extrato()
c2.gerar_extrato()
