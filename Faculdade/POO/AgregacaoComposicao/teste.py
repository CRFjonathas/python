from classes.Cliente import Cliente
from classes.Conta import Conta

cliente1 = Cliente("09707602562", "Jonathas", "Rua Formosa São João")
cliente2 = Cliente("01234567890", "Maria Cecilia", "Rua Formosa São João")

conta1 = Conta(cliente1, 12345, 10000)
conta2 = Conta(cliente2, 54321, 0)

conta1.gerar_saldo()

conta1.depositar(5000)
conta1.sacar(500)
conta1.transfere_valor(conta2, 800)

# OBJETO.ATRIBUTO.METODO(OBJETO.ATRIBUTO)
conta1.extrato.gerar_extrato(conta1.numero)

conta1.gerar_saldo()