'''def mostraLinha():
    print('-'*30)
'''

'''
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


#Programa Principal
mensagem('Curso em video')
mensagem('Aprenda python')
mensagem('Gustavo Guanabara')
'''

'''
def add(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('-'*30)


# Programa Principal
add(4, 5)
add(8, 9)
add(2, 1)
add(98, 8)
'''

'''
def contador(*num):
    #for valor in num:
     #   print(f'{valor}', end=' ')
    #print('FIM!')

    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam}')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 5, 6, 3)
'''

'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 4, 2, 5]
dobra(valores)
print(valores)
'''


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
