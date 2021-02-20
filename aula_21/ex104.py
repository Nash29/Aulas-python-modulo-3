'''Crie um programa que tenha a FUNÇÃO LEIAINT(), que vai funcionar de forma semelhante a função INPUT() do Python,
só que fazendo a VALIDAÇÃO para aceitar apenas um valor numerico.
EX: n = leiaInt('Digite um n')'''


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))  # 'n' recebe a mensagem
        if n.isnumeric():  # se 'n' for um numero
            valor = int(n)  # entao valor vai receber o int de 'n'
            ok = True  # E 'ok' passa a receber TRUE
        else:  # Se nao
            print('\033[0;31mERRO! Digite um numero inteiro válido.\033[m')
        if ok:  # Se 'ok' for TRUE
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}.')
