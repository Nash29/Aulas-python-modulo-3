'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)# Adiciona o numero 7
num.sort()# Coloca os numeros em ordem crescente
num.sort(reverse=True)# Coloca os numeros em ordem decrescente
num.insert(2, 0)# na posição 2 ele adiciona o valor 0
num.pop(2)#POP vazio elemina o ultimo elemento//POP com valor dentro elimina o valor que estiver dentro da casa selecionada
num.remove(2)# Elimina o valor selecionado como o POP
if 5 in num:
    num.remove(5)
else:
    print('Não achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''
#----------------------------------------------------------------------

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

#-------------------------------------------------------------------------

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')'''

#-------------------------------------------------------------------------

a = [2,3,4,7]
#b = a #Ligação de uma lista na outra
b = a[:]#COPIA de uma lista para outra
b[2] = 8 #Muda o valor nas duas listas quando é ligação// quando for copia ele muda apenas em um valor
print(f'Lista A: {a}')
print(f'Lista B: {b}')