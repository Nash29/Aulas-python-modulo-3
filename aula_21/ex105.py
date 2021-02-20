'''Faça um programa que tenha uma FUNÇÃO NOTAS() que pode receber varias notas de alunos e vai retornar um DICIONARIO
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A media da turma
- A situação (opcional)

Adicione também as DOCSTRINGS da função'''


def notas(*n, sit=False):
    '''
    -> Função para analizar notas e situações de varios alunos
    :param n: Uma ou mais notas dos alunos (aceita varias).
    :param sit: Valor opcionais, indicando se deve ou não adicionar a situação.
    :return: Dicionario com varias informações sobre a situação da turma.
    '''
    r = dict()  # Dicionario
    r['total'] = len(n)  # Pega a quantidade de numeros digitados
    r['maior'] = max(n)  # Pega o maior valor
    r['menor'] = min(n)  # Pega o menor valor
    r['media'] = sum(n)/len(n)  # Soma todos os numeros e divide pela qunatidade de numeros digitados
    if sit:  # Se 'sit' for TRUE
        if r['media'] > 7:  # Se media for maior que 7
            r['situação'] = 'BOA'
        elif r['media'] >= 5:  # Se media for maior que 5
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa Principal
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)
