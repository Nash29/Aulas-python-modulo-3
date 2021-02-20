'''Faça um programa que tenha um função chamada "area()", que receba as dimensões de um terreno
regular(largura e comprimento) e mostre a AREA DO TERRENO'''


def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg}x{comp} é de {a}m².')


print('Controle de Terrenos')
print('-'*30)
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (M): '))
area(l, c)
