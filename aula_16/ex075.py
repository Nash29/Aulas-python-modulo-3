'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A)Quantos vezes apareceu o valor 9
B)Em que posição foi digitado o primeiro valor 3
C)Quais foram os números pares'''

num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite main um numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')#Conta quantas vezes apareceu o numero 9
if 3 in num:# Se 3 estiver em numero
    print(f'O valor 3 apareceu no {num.index(3)+1}ª posição')#pega a posição e adiciona +1 pois começa no 0
else:
    print('O valor 3 não foi digitado')# caso não tenha o valor 3
print(f'Os valores pares digitados foram', end=' ')#Apenas frase
for i in num:
    if i % 2 == 0:
        print(i, end=' ')#Pega os numeros pares e coloca em sequencia