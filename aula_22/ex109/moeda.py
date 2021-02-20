#OBS: return res if not formato else moedas(res) e return res if formato is False else moedas(res) É A MESMA COISA DE FORMAS DIFERENTES


def metade(preco=0, formato=False):
    '''
    -> Descrição do código
    :param preco: Preço do produto
    :param formato: Se formato for FALSO passa apenas o valor no padrão PY, se for VERDADEIRO passa o valor em formato de moeda
    :return: Retorna metade do preço
    '''
    res = preco / 2
    return res if not formato else moedas(res)  # Retorna 'res' se não format senão retorna no formato moeda


def dobro(preco=0, formato=False):
    '''
    -> Descrição do código
    :param preco: Preço do produto
    :param formato: Se formato for FALSO passa apenas o valor no padrão PY, se for VERDADEIRO passa o valor em formato de moeda
    :return: Retorna o dobro do preço
    '''
    res = preco * 2
    return res if not formato else moedas(res)  # Retorna 'res' se não format senão retorna no formato moeda


def aumentar(preco=0, taxa=0, formato=False):
    '''
    -> Descrição do código
    :param preco: Preço do produto
    :param taxa: Taxa de aumento do salario nesse caso de 10%
    :param formato: Se formato for FALSO passa apenas o valor no padrão PY, se for VERDADEIRO passa o valor em formato de moeda
    :return: Retorna o aumento com a taxa de 10%
    '''
    res = preco + ((preco * taxa) / 100)
    return res if formato is False else moedas(res)  # Retorna res 'se' format é falso senão retorna no formato moeda


def diminuir(preco=0, taxa=0, formato=False):
    '''
    -> Descrição do código
    :param preco: Preço do produto
    :param taxa: Taxa de diminuição do salario nesse caso de 13%
    :param formato: Se formato for FALSO passa apenas o valor no padrão PY, se for VERDADEIRO passa o valor em formato de moeda
    :return: Retorna o diminuição com a taxa de 13%
    '''
    res = preco - ((preco * taxa) / 100)
    return res if formato is False else moedas(res)  # Retorna res 'se' format é falso senão retorna no formato moeda


def moedas(preco=0, moeda='R$'):
    '''
    -> Descrição do código
    :param preco: Preço do produto
    :param moeda: Passa para o formato moeda
    :return: Retorna o valor com o fortamo monetario, com duas casas depois da virgula e virgula(,) no lugar do ponto(.)
    '''
    res = f'{moeda}{preco:.2f}'.replace('.', ',')  #Subistitui '.' por ','
    return res
