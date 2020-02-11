s = 0
for x in range (0, 6):
    n = int(input('Digite um numero: '))
    if n %2 == 0:
        s += n

print('A soma entre os numeros pares foi: {}'.format(s))