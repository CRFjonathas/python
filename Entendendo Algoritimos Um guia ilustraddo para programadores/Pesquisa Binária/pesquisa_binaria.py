def pesquisa_binaraia(lista, item):
    baixo = 0                                       # Alto e baixo acompanham a parte da lista que você está proucurando.
    alto = len(lista)                               # Alto e baixo acompanham a parte da lista que você está proucurando.

    while baixo <= alto:                            # Enqunato ainda não conseguiu chegar a um único elemento...
        meio = (baixo + alto) / 2                   # ... Verifica o elemento central.
        chute = lista[meio]

        if chute == item:                           # Acha o item.
            return meio
        if chute > item:                            # O chute foi muito alto.
            alto = meio - 1
        else:                                       # O chute foi muito baixo.
            baixo = meio + 1

    return None                                     # O item não existe.

minha_lista = [1, 3, 5, 7, 9]                       # Vamos testa-lo!

print(pesquisa_binaraia(minha_lista, 3))            # Lembre-se, as lista começam no 0. O proximo endereço tem indicie 1.
print(pesquisa_binaraia(minha_lista, -1))           # "None" significa nulo em Python. Ele indica que o item não foi encontado.