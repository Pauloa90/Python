print('-'*20)
print('Gerador de Pa!')

p = int(input('Primeiro Termo: '))
r = int(input('Razao da Pa: '))

termo = p
c = 1

while c <= 10:
    print('{} - '.format(termo), end='')
    termo += r
    c += 1

