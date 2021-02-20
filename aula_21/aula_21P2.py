# INTERATIVE HELP
'''help(print)'''

# DOCSTRINGS
'''
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)# mostra o que esta nas """dentro das aspas"""
'''

# ARGUMENTOS OPCIONAIS
"""
def somar(a=0, b=0, c=0):
    '''

    :param a:
    :param b:
    :param c:
    :return:
    '''

    s = a + b + c
    print(f'A soma vale {s}')


somar(4, 2, 6)
somar(2, 6)
somar()
"""

#ESCOPO DE VARIAVEIS
"""
def teste():
    n1 = 4
    print(f'N1 local vale {n1}')


teste()
n1 = 2
print(f'N1 global vale {n1}')
"""

# RETORNO DE VALORES
'''
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 5, 4)
r2 = soma(2, 6)
r3 = soma(3)
print(f'Os resultados foram {r1}, {r2} e {r3}')
'''

#EXEMPLOS
'''
def fatorial(num=1):
    f = 1
    for cont in range(num, 0, -1):
        f *= cont
    return f


f1 = fatorial(5)
f2 = fatorial(13)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')
'''


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('É par')
else:
    print('É impar')
