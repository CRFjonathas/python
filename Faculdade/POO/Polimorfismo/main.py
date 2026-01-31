from classes.ContaCliente import ContaCliente
from classes.Banco import Banco
from classes.ContaComum import ContaComum
from classes.ContaRemunerada import ContaRemunerada

banco1 = Banco(999, "Teste")

conta_cliente = ContaCliente(1, 0.01, 0.1, 2000, 0.05)
conta_comum = ContaComum(2, 0.01, 0.1, 2000, 0.05)
conta_remunerada = ContaRemunerada(3, 0.01, 0.1, 2000, 0.05)

banco1.adciona_conta(conta_cliente)
banco1.adciona_conta(conta_comum)
banco1.adciona_conta(conta_remunerada)

banco1.calcular_rendimento_mensal()
banco1.imprime_saldo_contas()