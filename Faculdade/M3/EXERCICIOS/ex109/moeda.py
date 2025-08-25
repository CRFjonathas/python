def metade(preço, formato=False):
    resultado = preço / 2
    return resultado if not formato else moeda(resultado)

def dobro(preço, formato=False):
    resultado = preço * 2
    return resultado if not formato else moeda(resultado)

def aumentar(preço, porcentagem, formato=False):
    aumento = preço + (preço * porcentagem /100)
    return aumento if not formato else moeda(aumento)

def diminuir(preço, porcentagem, formato=False):
    desconto = preço - (preço * porcentagem /100)
    return desconto if not formato else moeda(desconto)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
