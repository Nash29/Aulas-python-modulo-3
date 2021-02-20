'''Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas
de cada aluno individualmente'''

ficha = list()

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2

    ficha.append([nome, [n1, n2], media])
    decisao = ' '
    while decisao not in 'SN':
        decisao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if decisao == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*20)
for i, a in enumerate(ficha):
    # 4 espaços começando pela esquerda, 10 começando pela esquerda, 8 espaços começando pela direita e com 1 casa depois da virgula
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Msotrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1: # -1 pq começa no 0
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
