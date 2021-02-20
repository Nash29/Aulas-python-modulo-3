'''Faça um MINI-SISTEMA que utilize o INTERACTIVE HELP do Python. O usuario vai digitar o COMANDO e o MANUAL vai aparecer.
Quando o usuario digitar a palavra "FIM", o programa se ENCERRARA.
OBS: use cores'''
from time import sleep

c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m'      # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)  #Frase que aparece depois da função da biblioteca
    print(c[6], end='')  # A documentação fica branco
    help(com)  # Mostra as informações  das funções
    print(c[0], end='')
    sleep(2)  # Tempo de 2s para aparecer a proxima frase na tela


def titulo(msg, cor=0):
    tam = len(msg) + 4  # Adiciona mais 4 tracinhos
    print(c[cor], end='')  # Cor vermelho
    print('~'*tam)
    print(f'  {msg}')  # titulo
    print('~'*tam)
    print(c[0], end='')
    sleep(1)  # Tempo de 1s para aparecer a proxima frase na tela


#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)  # Cor amarelo
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)  # Cor vermelho
