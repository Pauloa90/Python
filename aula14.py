c = 0
while c < 10:
    c += 1
    print(c)

n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()

print('Fim')