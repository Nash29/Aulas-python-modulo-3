'''
Tuplas ()
listas [] ou lista = list()
Dicionarios {} ou dados = dict()
'''

'''
pessoas = {'nome': 'Murilo', 'sexo': 'M', 'idade': 20}
# print(pessoas.items()) # Mostra tanto keys quanto value
# print(pessoas.keys()) # Mostra o nome das chaves
# print(pessoas.values()) # Mostra os valores

# del pessoas['sexo'] # Deleta sexo
# pessoas['nome'] = 'Marcos' # Troca o valor de nome
# pessoas['peso'] = 98.5 # Adiciona um novo valor
for k, v in pessoas.items():
    print(f'{k} = {v}')
    
'''

'''
# ADICIONANDO UM DICIONARIO DENTRO DE UMA LISTA

brasil = list()
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

# print(brasil[1]['uf']) # Mostra: São Paulo
'''

estado = dict()
brasil = list()
for c in range(3):
    estado['uf'] = str(input('Unidade Fedrativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
# print(brasil)

for e in brasil: #Para cada e(estado) in(em) Brasil
    for k, v in e.items(): # k(Keys) // v(Values) .items pega tudo
        print(f'O campo {k} tem valor {v}')
