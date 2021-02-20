'''Aprimore o DESAFIO 093 para que ele funcinone com VARIOS JOGADORES, incluindo um sistema de visualização
de DESTALHES DO APROVEITAMENTO de cada jogador'''

time = list()
dados = dict()
partida = list()

#LÊ OS DADOS
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    partida.clear()
    for i in range(tot):
        partida.append(int(input(f'   Quantos gols na partida {i+1}? ')))
    print('-'*20)
    dados['gols'] = partida[:]#Copia a quantidade de gols na partida e manda para o "dict" dados
    dados['total'] = sum(partida) #Jogador total recebe a soma so que esta em partidas
    time.append(dados.copy()) #copia os dados para o time
    while True:
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)

#MOSTRA OS RESULTADOS
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')# 4 Caractere centralizado a direita
    for d in v.values():
        print(f'{str(d):<15}', end='')# 15 caratere alinhado a esquerda
    print()
print('-'*30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']): # i = indice, g = gols
            print(f'   No jogo {i+1} fez {g} gols.')# Mostra qual jogo foi e o numero de gols
    print('-'*30)
print('<< VOLTE SEMPRE >>')
