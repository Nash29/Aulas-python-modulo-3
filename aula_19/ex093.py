'''Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL.
O programa vai ler o NOME DO JOGADOR e QUANTAS PARTIDAS ele jogou.
Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA.
No final, tudo isso sera quardado em um DICIONARIO, incluindo o TOTAL DE GOLS feitos durante o campeonato'''

dados = dict()
partida = list()

dados['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for i in range(tot):
    partida.append(int(input(f'   Quantos gols na partida {i+1}? ')))
print('-'*20)
dados['gols'] = partida[:]
dados['total'] = sum(partida) #Jogador total recebe a soma so que esta em partidas

print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
