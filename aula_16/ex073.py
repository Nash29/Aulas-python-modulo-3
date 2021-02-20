'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Compeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
A) Apenas os 5 primeiros colocados.
B)Os ultimos 4 colocados da tabela
C)Uma lista com os times em ordem alfabética
D)Em que posição na tabela está o time da Chapecoense'''


colocados = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio',
             'Flamengo', 'Corinthians', 'Internacional', 'Cruzeiro',
             'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Fluminense',
             'Chapecoense', 'Bahia', 'Goias', 'Guarani',
             'Sport', 'Portuguesa', 'Atlético Paranaense', 'Vitória')
print('-='*20)
print(f'Lista de times do Brasileirão {colocados}')
print('-='*20)
print(f'Os 5 primeiros colocados são {colocados[:5]}')
print('-='*20)
print(f'OS 4 últimos são {colocados[-4:]}')#De tras pra frente começa do 1 e não do 0
print('-='*20)
print(f'Times em ordem alfabética: {sorted(colocados)}')
print('-='*20)
print(f'O Chapecoense está em {colocados.index("Chapecoense")+1}ª posição')# Acha a posição onde a frase esta e o +1