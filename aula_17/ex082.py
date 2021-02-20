'''Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteudo das três listas geradas'''

valores = []
pares = list()
impares = list()
while True:
    v = (int(input('Digite um número: ')))
    valores.append(v)
    escolha = ' '
    while escolha not in 'SN': #Não estiver
        escolha = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if escolha in 'N':# Estiver
        break
for i, v in enumerate(valores):# i = indice // v = valor
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
