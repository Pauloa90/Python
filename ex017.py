import math

n1 = float(input('Digite o comprimento do cateto oposto: '))
n2 = float(input('Digite o comprimento do cateto adjacente: '))
h = math.pow(n1, 2) + math.pow(n2, 2)
hipo = math.pow(h, 1/2)
print('O valor da hipotenusa é {:.2f}'.format(hipo))
