'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços, organizando os dados em forma tabular'''

print('=='*25)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('=='*25)

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20,
             'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for pos in range(0, len(listagem)):# LEN = pega a numeração de cada frase e valor
    if pos % 2 == 0:# Se os valores for PAR ou seja apartir do 0
        print(f'{listagem[pos]:.<30}', end='')# < = Joga os valores pra ESQUERDA/ . = para colocar o ponto depois da frase em um espaçamento de 30
    else:
        print(f'R${listagem[pos]:>7.2f}')# > = joga os valores IMPARES pra direita/ 7 = espaçamento entre o R$ e o VALOR/.2f = duas casas depois da virgula
print('=='*25)
