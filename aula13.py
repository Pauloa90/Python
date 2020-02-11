for x in range (0, 10, 2):
    print(x)
print('FIM')

for x in range (6, 0, -1):
    print(x)

n = int(input('DIgite um numero: '))
for x in range (0, n+1):
    print(x)

i = int(input('DIgite inicio: '))
f = int(input('DIgite fim: '))
p = int(input('DIgite passo: '))

for x in range (i, f+1, p):
    print(x)

s = 0
for x in range (0, 5):
    n = int(input('Digite um valor varias vezes: '))
    s += n
print('Fim')
print('O somatorio foi {}'.format(s))