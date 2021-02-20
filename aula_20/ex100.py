'''Faça um programa que tenha uma LISTA chamada NUMEROS e duas FUNÇÕES chamdas "sorteio()" e "somaPar()".
A primeira função vai sortear 5 NUMEROS e vai coloca-los dentro da lista e a segunda função vai mostrar a SOMA
entre todos os valores PARES sorteados pela função anterior'''

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(5):# Conte 5 numeros
        n = randint(1, 10)# De 1 a 10
        lista.append(n)# vai adicionando os valores na lista
        print(f'{n} ', end='')
        sleep(0.3)# Tempo de aparição de cada num
    print('PRONTO')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


num = list()
sorteia(num)
somaPar(num)
