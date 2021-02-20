'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso'''

contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito',
            'nove', 'dez', 'onze', 'doze',
            'treze', 'quatorze', 'quize', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:#Qaundo quiser repetir 1 vez ou mais vezes
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:#Se o numero estiver entre 0 a 20
        break# programa termina
    print('Tente novamente.', end='')# Se não aparecera essa frase e o WHILE recomeça
print(f'Você digitou o número {contagem[num]}')# Se for verdadeiro vai pegar o numero que o usuario digitou e vai pegar o nome na CONTAGEM
