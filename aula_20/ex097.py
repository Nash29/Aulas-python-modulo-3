'''Faça um programa que tenha uma função chamada "escreva()", que recebeu um texto qualquer como PARAMETROA e mostre
uma mensagem com tamanho adaptavel

EX:
escreva('Ola, Mundo!')

Saida:
~~~~~~~~~~~~~~~~~~~~~~~~
ola mundo!
~~~~~~~~~~~~~~~~~~~~~~~~'''


def escreva(msg):
    tam = len(msg) + 4# Pega o tamanho da mensagem e adiciona mais 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


escreva('Murilo Nogueira')
escreva('Curso de python no youtube')