nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em mainusculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))