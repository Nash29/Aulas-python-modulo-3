'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo que
o vencedor tirouo maior numero no dado'''

from random import randint
from time import sleep
import operator
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}#Dicionario
ranking = list()

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou o {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)#Ordena pela sequencia de numero usando o itmgetter
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):# i(indice), v(valor)
    print(f'   {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
