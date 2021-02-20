'''teste = list()
teste.append('Murilo')
teste.append(20)
galera = list()
galera.append(teste[:])#Cópia
teste[0]= 'Natalia'
teste[1] = '21'
galera.append(teste[:])#Cópia
print(galera)'''

#-------------------------------------------------------------------------
#galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
'''print(galera[2][1])# A primeira mostra a lista que esta nessa posição // Segundo mostra o conteudo que esta dentro da lista'''
'''for p in galera:# Para cada P = pessoa// in = em // galera
    print(f'{p[0]} tem {p[1]} anos de idade')#Mostra as pessoa na lista galera'''

#-------------------------------------------------------------------------
galera = list()#Estrutura principal
dado = list()# Estrutura ausiliar que vai pegar os dados para mandar para estrutura principal
totmai = totmen = 0

#Bloco lê os dados e joga dentro de galera // Apagando os dados cada vez que eu faço o laço
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])#Copia dados para galera
    dado.clear()

#Analisa para ver se o cara é maior ou menor de idade
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e tantos {totmen} menores de idade')
