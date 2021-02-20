'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Lista 3 por 3 // Ps: ex86 tem a explicação
par = mai = somacol = 0

# FOR DE ALIMENTAÇÃO, coloca os valores dentro da matriz
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# FOR para mostrar a estrutura na tela
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print('-='*30)

print(f'A soma dos valores pares é {par}')
# Coluna fica a mesma só a linha que muda
for l in range(3):
    somacol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacol}')

# Linha fica a mesma só a coluna que muda
for c in range(3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')

