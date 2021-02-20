lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche[-2])
print(lanche[1:3])
print(lanche[1:])

print(len(lanche))

#for i in range(0, len(lanche)):
   # print(f'Eu vou comer {lanche[i]}')

#for c in lanche:
 #   print(f'Eu vou comer {c}')

#for pos, comida in enumerate(lanche):
 #   print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

print(sorted(lanche)) # Em ordem

print('--'*30)

a = 5, 2, 4
b = 5, 8, 1, 2
c = a + b
print(c.count(5))
print(c)
print(c.index(2))# pega a posição

print('--'*30)

pessoa = 'Murilo', 19, 'M', 61.42
print(pessoa)