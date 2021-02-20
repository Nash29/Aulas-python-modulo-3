'''Faça um programa que leia nome e pso de varias pessoas, guardando tudo em um lista. No final, mostre:
A) Qauntas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves'''

lista = list()
dado = list()

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        mai = men = dado[1] #Peso
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    lista.append(dado[:]) #Adiciona os dados dentro da lista
    dado.clear() #Limpa os dados depois que passar pra lista

    escolha = ' '
    while escolha not in 'NS':
        escolha = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if escolha == 'N':
        break

print('-='*30)
print(f'A todo você cadastrou {len(lista)} pessoas') #Pega o numero das listas
print(f'O maior peso foi de {mai}Kg. Peso de', end=' ')
for p in lista: #Para cada p(pessoa) em lista
    if p[1] == mai: #Peso for == maior
        print(f'[{p[0]}]', end=' ')#Mostra o nome delas
print(f'\nO menor peso foi de {men}Kg. Peso de', end=' ')
for p in lista:#Para cada p(pessoa) em lista
    if p[1] == men:#Peso for == menor
        print(f'[{p[0]}]', end=' ')#Mostra o nome delas
