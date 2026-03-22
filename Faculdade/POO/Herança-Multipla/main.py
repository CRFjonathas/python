from classes.Cliente import Cliente
from classes.Conta import Conta
from classes.ContaRemuneradaPoupanca import ContaRemuneradaPoupanca


from rich.traceback import install
install()

cliente1 = Cliente("123", "Jonathas", "Rua X")
cliente2 = Cliente("321", "Mariely", "Rua Y")
cliente3 = Cliente("102030", "Maria Cecília", "Rua Z")

conta1 = Conta(cliente1, 1, 3000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaRemuneradaPoupanca(cliente3, 3, 10000, 0.1)

conta3.remuneraConta()

conta1.depositar(500)
conta1.transferir_valor(conta3, 1000)
conta2.sacar(700)
conta2.transferir_valor(conta3, 300)



conta1.extrato.gerar_extrato(conta1)
conta2.extrato.gerar_extrato(conta2)

conta3.extrato.gerar_extrato(conta3)