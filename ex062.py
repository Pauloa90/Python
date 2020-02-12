print('-'*20)
print('Gerador de PA: ')

p = int(input('Primeiro termo: '))
r = int(input('Razao da PA: '))
amais = 10
total = 0
termo = p

c = 1

while amais != 0:
    total += amais
    while c <=total:
        print('{} - '.format(termo), end='')
        termo += r
        c += 1
    amais = int(input('Quantos termo a mais deseja ver: '))