def voto(ano_nasc):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


# Programa principal

nascimento = int(input('Ano de nascimento: '))
print(voto(nascimento))