'''Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem UM PARAMETRO a mais, informativo
se o valor retornado por elas vai ser ou não formatado pela função MOEDA(), desenvolvida no DESAFIO 108'''

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moedas(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moedas(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}')
