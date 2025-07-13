from random import randint

computador = randint(0, 5)

print("-=-" *20)
print("Vou pensar em um numero entre 0 e 5. Tente advinhar...")
print("-=-" *20)

jogador = int(input("Em que numero pensei? "))

if jogador == computador:
    print("PARABENS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no numero {} e não no numero {}".format(computador, jogador))