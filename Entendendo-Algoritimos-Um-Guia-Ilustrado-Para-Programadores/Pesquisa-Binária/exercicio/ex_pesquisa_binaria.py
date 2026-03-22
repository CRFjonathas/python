def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    passos = 0

    while baixo <= alto:
        meio = (alto + baixo) // 2
        chute = lista[meio]

        if chute == item:
            passos += 1
            return f"Foram precisos de {passos} passos para encontrar o numero {meio + 1}"
        if chute > item:
            alto = meio - 1
            passos += 1
        else:
            baixo = meio + 1
            passos += 1

    return f"Valor não encontrado na lista."


lista = list(range(1, 1000001))

num = int(input("Qual numero você deseja encontar na lista? "))

print(pesquisa_binaria(lista, num))