'''Crie um programa onde o usuario digite uma expressão qualquer que use parenteses. Seu aplicativo devera analizar
se a expressão passada esta com os parenteses abertos ou fechados na ordem correta'''

expr = str(input('Digite a expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida!')
else:
    print('Sua expressão esta errada!')
