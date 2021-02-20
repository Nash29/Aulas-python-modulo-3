'''Faça um programa que leia nome e media de um aluno, guardando também a situação em um dicionario.
No final, mostre o conteudo da estrutura na tela'''

dados = dict()

dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média do {dados["nome"]}: '))
if dados['media'] < 4:
    dados['situação'] = 'Reprovado'
elif 4 <= dados['media'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Aprovado'

print('-'*20)
for k, v in dados.items(): # k = key, v = value
    print(f'{k} é igual a {v}')

