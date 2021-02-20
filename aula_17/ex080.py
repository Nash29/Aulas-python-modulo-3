'''Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, ja na posição
correta de inserção (sem usar o SORT()).
No final, mostre a lista ordenada na tela'''

list = []

for v in range(5):
    n = int(input('Digite um valor: '))
    if v == 0 or n > list[-1]: #Se o valor for = 0 OU Se o numero for maior que o numero que esta no ultimo elemento
        list.append(n) # Adiciona um numero na lista
        print('Adicionado ao final da lista...')
    else:# Ele vai da posição '0' até a ultima posição que no caso 'len(list)'
        pos = 0
        while pos < len(list):
            if n <= list[pos]: #Vou verificar dentro de cada posição se o numero que eu quero enserir é <= a ele
                list.insert(pos, n)# Na posição 'pos' o valor 'n'
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {list}')
