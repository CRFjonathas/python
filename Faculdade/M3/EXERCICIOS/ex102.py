def fatorial(f, show=False):
    """
    Calcula o fatorial de um número.
    :param f: número a ser calculado o fatorial
    :param show: (opcional) mostrar ou não a conta
    :return: valor do fatorial de f
    """
    f = 1
    for c in range(f, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# programa principal
print(fatorial(10, show=True))