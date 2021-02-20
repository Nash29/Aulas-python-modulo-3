'''Crie um programa que tenha uma FUNÇÃO fatorial() que receba dois parametros: o primeiro que indique o NUMERO a calcular
e o outro chamado SHOW, que sera um valor LÓGICO(opcional) inidicando se sera mostrado ou não na tela o processo
de calculo do fatorial'''


def fatorial(num=1, show=False):
    '''
    -> Calcula o fatorial do numero
    :param num: Calcula o fatrorial de um numero.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um numero n.
    '''

    f = 1
    for cont in range(num, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= cont

    return f


# Programa Principal
print(fatorial(5, show=True))
help(fatorial)
