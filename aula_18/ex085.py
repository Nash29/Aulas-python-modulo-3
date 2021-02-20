'''Crie um prgrama onde o usuario possa digitar sete valores numéricos e cadastre-os em uma lista unica que mantenha
 separados os valores pares e impares. No final, mostre os valores pares e impares em odem crescente'''
'''
# MINHA RESOLUÇÃO
valor = list()
tot = list()
for i in range(7):
    valor.append(int(input(f'Digite o {i+1}º valor: ')))
    tot.append(valor[:])
    valor.clear()

print('-='*15)
tot.sort()
print('Os valores pares digitados foram: ', end='')
for p in tot:
    if p[0] % 2 == 0:
        print(f'{p}', end=' ')

print('\nOs valores impares digitados foram: ', end='')
for p in tot:
    if p[0] % 2 == 1:
        print(f'{p}', end=' ')
'''
# PROF RESOLUÇÃO
num = [[], []] #2 listas dentro de 1 lista
valor = 0
for c in range(7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor) #Coloca o par na lista 0
    else:
        num[1].append(valor)#Coloca o impar na lista 1
print('-='*30)
num[0].sort() #Sort ordena o valor crescentemente
num[1].sort()

print('Os valores pares digitados foram: {}'.format(num[0]))
print('Os valores pares digitados foram: {}'.format(num[1]))
