from classes import Cliente
from classes import Conta

cliente1 = Cliente("09707602562", "Jonathas", "Rua Formosa São João")
cliente2 = Cliente("01234567890", "Maria Cecilia", "Rua Formosa São João")

conta1 = Conta([cliente1, cliente2], 12345, 10000)

conta1.gerar_saldo()
conta1.depositar(5000)
conta1.gerar_saldo()