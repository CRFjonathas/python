from classes.Cliente import Cliente
from classes.Conta import Conta
from classes.ContaEspecial import ContaEspecial
from rich.traceback import install

install()

cliente1 = Cliente("123", "João", "Rua X")
cliente2 = Cliente("321", "Maria", "Rua Y")
cliente3 = Cliente("102030", "Jonathas", "Platafoma")

conta1 = Conta(cliente1, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaEspecial(cliente3, 3, 4000, 500)

conta1.depositar(300)
conta1.transferir_valor(conta2, 500)

conta2.sacar(700)

conta3.extrato.gerar_extrato(conta3)
conta1.extrato.gerar_extrato(conta1)
conta2.extrato.gerar_extrato(conta2)