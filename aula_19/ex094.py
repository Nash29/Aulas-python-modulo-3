'''Crie um programa que leia NOME, SEXO e IDADE de VARIAS PESSOAS, guardando os dados de cada pessoa em um DICIONARIO
e todos os dicionarios em uma LISTA. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A MEDIA de idade do grupo
C) Uma lista com todas as MULHERES
D) Uma lista com todas as pessoas com IDADE acima da MEDIA'''

dados = dict()
lista = list()
soma = media = 0

#LEITURA DE DADOS
while True:
    dados['nome'] = str(input('Digite seu nome: '))
    while True:
        dados['sexo'] = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
        if dados['sexo'] in 'MF':# Se sexo for "MF" o programa continua
            break
        print('ERRO! Por favor, digite apenas M ou F')#Se não aparece essa mensagem e retorna

    dados['idade'] = int(input('Digite sua idade: '))
    soma += dados['idade']# Soma as idades
    lista.append(dados.copy()) #Lista copia dados

    while True:
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Resposta apenas S ou N')
    if resp == 'N': #Sai do programa
        break
print('-='*30)
#RESULTADO

print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')

media = soma / len(lista)
print(f'B) A média de idade é de {media:5.2f} anos.')# 5 casas ao todo sendo duas depois da virgula

print('C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'Ff': #Se 'Ff' estiver em sexo
        print(f'{p["nome"]}, ', end='') #Vai pegar os nomes das mulheres
print()

print('D) Lista das pessoas que estão acima da media: ')
for p in lista:
    if p['idade'] >= media: #Se a idade da pessoa for maior que a media entre eles
        print('    ', end='')
        for k, v in p.items(): #Pega a key e o value
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
