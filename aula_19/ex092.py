'''Crie um progrma que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os(com IDADE) em um dicionario
se por acaso a CTP5(carteira de trabalho) for diferente de ZERO, o dicionario recebera tambem o ANO DE CONTRATAÇÃO e o SALARIO.
Calcule e acrescente, alem da IDADE, com quantos naos a pessoa vai se APOSENTAR'''

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: ')) #Ano de nascimento não vai esta no dicionario
dados['idade'] = datetime.now().year - nasc #Pega o ano atual menos o nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    #Pega o ano de contratação + 35 depois - o ano atual o que sobrar ele soma com a idade
    #Ex: 2020 + 35 = 2055 - 2020 = 35 + 20 = 55 anos
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('-='*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')

