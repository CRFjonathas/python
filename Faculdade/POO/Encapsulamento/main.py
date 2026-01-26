from classes.conta import Conta

c1 = Conta(1, 1000)
c2 = Conta(2, 50)
c1.sacar(200)

c1.saldo = -1500

print(f"Até agora temos {Conta.get_total_contas()} conta(s) criada(s)")
print(f"Muito Obrigado por ser cliente do {Conta.nome_banco()}")

c1.gerar_saldo()
print(f"Conta 2 com R$ {c2.saldo}")