s = 0
n = int(input('Digite um numero para saber se ele é primo: '))
for x in range(1, n + 1):
    if n % x == 0:
        s += 1
if s == 2:
    print('O numero {} é Primo'.format(n))
else:
    print('O numero {} nao é primo'.format(n))