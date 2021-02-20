'''Faça um programa que tenha uma função chamada "contador()", que receba três PARAMETROS: inicio, fim e passo e realize a contagem
Seu programa tem que realizar TRES CONTAGENS atraves da função criada:

A) De 1 ate 10, de 1 em 1
B) De 10 ate 0, de 2 em 2
C) Uma contagem personalizada'''

from time import sleep


def linha():
    print('-='*20)


def contador(i, f, p):
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if p < 0:# Caso o passo seja negativo
        p *= -1
    if p == 0:# Caso o passo seja 0
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


#Programa principal
contador(1, 10, 1)# Valores da primeira contagem
contador(10, 0, 2)# Valores da segunda contagem
linha()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)# Pega os valores que a pessoas escolher
