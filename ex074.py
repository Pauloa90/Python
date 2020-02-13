import random

# Sorteando 5 numeros
pc = random.sample(range(0, 10), 5)
# Outra opcao: pc = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

# Transformando em Tupla
pc = tuple(pc)

maior = pc[0]
menor = pc[0]

# Obtendo o maior 
for x in pc:
    if x > maior:
        maior = x

# Obetendo o menor:
    for x in pc:
        if x < menor:
            menor = x
print(f'A tupla sorteado foi: {pc}')
print(f'O maior numero dentro da tupla foi o {maior}')
print(f'O menor numero dentro da tupla foi o {menor}')
