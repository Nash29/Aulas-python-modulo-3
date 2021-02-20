'''Crie um programa onde o usuario possa digitar varios valores numéricos e cadastre-os em uma lista.
Caseo o numero ja esxista la dentro, ele não esta adicionado. No final, serão exibidos todos
os valores unicos digitados, em ordem crescente'''

valores = list()

while True:
    v = (int(input('Digite um valor: ')))
    if v not in valores:#Não estiver
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = ' '
    while continuar not in 'SN':#Não estiver
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-='*25)
valores.sort()#Sort colocou os valores em sequencia
print(f'Você digitou os valores {valores}')
