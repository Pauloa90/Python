n = 0
s = 0
while True:
    n = int(input('Digite um numero: '))
    
    if n == 999:
        break
    s += n
print('A soma entre os numeros é {}'.format(s))
