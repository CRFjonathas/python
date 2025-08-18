from datetime import date

ano_atual = date.today().year

pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
pessoa['nascimento'] = int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Numero da carteira de trabalho: (0 se não tiver) '))

pessoa['idade'] = ano_atual - pessoa['nascimento']

if pessoa['CTPS'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (ano_atual - pessoa['contratação']))

print('-='*30)
for c, v in pessoa.items():
    print(f'    -{c} tem o valor de {v}')
