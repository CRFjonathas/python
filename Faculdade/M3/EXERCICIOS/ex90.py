alunos = dict()

alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Media de {alunos['nome']}: '))

print('-=' *30)
print(f'    - nome: {alunos['nome']}')
print(f'    - média: {alunos['media']}')

if alunos['media'] >= 7:
    alunos['situação'] = 'aprovado'
    print(f'    - situação: {alunos['situação']}')
elif alunos['media'] >= 5:
    alunos['situação'] = 'recuperação'
    print(f'    - situação: {alunos['situação']}')
else:
    alunos['situação'] = 'reprovado'
    print(f'    - situação: {alunos['situação']}')

print()