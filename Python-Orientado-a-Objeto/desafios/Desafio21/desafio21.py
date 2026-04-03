from rich import print
from classes.Caneta import Caneta

c1 = Caneta("vermelho")
c2 = Caneta("verde")
c3 = Caneta("azul")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto!")
c3.escrever("Vamos exercitar!")
