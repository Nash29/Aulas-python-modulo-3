'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, voce deve mostrar, para cada palavra, quais são as suas vogais'''

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:#P = pega cada frase das palavras
    print(f'\nNa palavra {p} temos -> ', end='')#Pega a frase e vai pulando de linha em linha
    for letra in p:# Letra pega cada letra da palavra
        if letra.lower() in 'aeiou':#Se a frase tiver a letra 'aeiou'//Deixa tudo em minusculo
            print(letra, end=' ')#As vogais vai aparecer