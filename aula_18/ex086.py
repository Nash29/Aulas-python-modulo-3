'''Crie um programa que crie uma matriz de dimeção 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formação correta'''


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Lista 3 por 3
# FOR DE ALIMENTAÇÃO, coloca os valores dentro da matriz
for l in range(3): #Linha
    for c in range(3): #Coluna
        # L -> mostra a posição da lista e C-> mostra qual valor sera colocado nela
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# FOR para mostrar a estrutura na tela
print('-='*30)
for l in range(3):
    for c in range(3):
        # Coloca os valores e deixa um do lado do outro
        print(f'[{matriz[l][c]:^5}]', end='')# :^5 -> Centraliza os valores com 5 casas decimais
    print() #Esse print quebra a linha depois de 3 valores

