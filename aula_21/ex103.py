'''Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois PARAMETROS OPCIONAIS: o NOME de um jogador
e quantos gols ele marcou. O programa devera ser capas de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha
sido informado corretamente'''


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa pincipal
nome = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():# Se g for numero
    g = int(g)# g recebe o int do g
else:
    g = 0# se não só fica 0
if nome.strip() == '':# Se nome só tiver espaços
    ficha(gol=g)# ficha só vai receber  gol
else:
    ficha(nome, g)# Se não ficha vai receber os dois valores
