'''Crie um programa que vai gerar cinco numeros aleatórios e colocar em um tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla'''
import random

numeros = (random.randint(1, 10)), (random.randint(1, 10)), (random.randint(1, 10)), \
          (random.randint(1, 10)), (random.randint(1, 10))
print('Os valores sortedos foram: ', end='')

for n in numeros:
    print(f'{n}', end=' ')# n -> pega todos os numeros de 'numeros', sim é necessario Murilo
print(f'\nO maior valor sorteado foi {max(numeros)}')#Pega o maior numero
print(f'O menor valor sorteado foi {min(numeros)}')#Pega o menor numero
