'''Faça um programa que tenha uma FUNÇÃO chamada "maior()", que receba varios PARAMETROS com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''
from time import sleep


def maior(*num):# Pega uma quantidade de numeros indefinidos
    cont = maior = 0
    print('-='*20)
    print('Analizando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)

        if cont == 0:# Necessario para achar o maior e menor
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


# Programa principal
maior(2, 9, 4, 6, 3, 7)
maior(4, 1, 7, 3)
maior(4, 0, 3)
maior(1, 9)
maior()
