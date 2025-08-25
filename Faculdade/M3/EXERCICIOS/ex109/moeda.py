def metade(preço):
    return preço / 2

def dobro(preço):
    return preço * 2

def aumentar(preço, porcentagem):
    aumento = (porcentagem / 100) * preço
    return preço + aumento

def diminuir(preço, porcentagem):
    desconto = (porcentagem / 100) * preço
    return preço - desconto

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
