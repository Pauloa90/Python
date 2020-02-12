lanche = ('Hamburguer', 'Suco', 'Salada', 'Pudim')
print(lanche[-2:])

# Tuplas sao Imutaveis!!!

for x in lanche:
    print(f'Eu vou comer {x}')
print(len(lanche))

for l in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[l]} na posicao {l}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

print(sorted(lanche))

a= (2, 5, 4)
b =(5, 6, 2)
c = a + b
print(c)
print(sorted(c))
print(len(c))

print(c.count(5))
print(c.count(2))
print(c.index(2,1))

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

del(pessoa)