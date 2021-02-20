'''Crie um programa que vai ler varios numeros e colocar em um lista. Depois disso, mostre:
A) Quantos numeros foram digitados
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e esta ou não na lista'''

valores = list()
while True:
    lista = int(input('Digite um valor: '))
    valores.append(lista)
    decisao = ' '
    while decisao not in 'SN':
        decisao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if decisao == 'N':
        break
print('-='*30)
valores.sort(reverse=True)

print(f'Os valores em ordem descrescente {valores}')
print(f'Você digitou {len(valores)} elementos')
if 5 in valores: # Se o 5 estiver dentro dos VALORES
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')
