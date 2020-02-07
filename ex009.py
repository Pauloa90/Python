n = int(input('Digite um numero: '))
c = 1
print('O numero escolhido foi: {}. Vamos ver a sua tabuada:'.format(n))
while c < 10:
    print('{} x {} = {}'.format(n, c, c * n))
    c += 1       

for i in range (10):
    print('{} x {} = {}'.format(n, i, i * n))