p = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razao da PA:  '))

c = 1
termo = p

while c < 11:
    print('{} '.format(termo), end='')
    termo += r
    c += 1
print('FIM')
