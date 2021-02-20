'''Crie um programa que tenha uma FUNÇÃO chamada VOTO() que vai receber como parametro de uma pessoa nascimento
de uma pessoa, retornando um valor literal indicado se uma pessoa tem voto NEATIVO, OPCIONAL ou OBRIGATÓRIO nas eleições'''


def voto(ano):
    from datetime import date

    print('-'*30)
    data_atual = date.today().year
    idade = data_atual - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 18 <= idade < 60:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif 16 <= idade < 18 or idade >= 60:
        return f'Com {idade} anos: VOTO OPCIONAL.'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
