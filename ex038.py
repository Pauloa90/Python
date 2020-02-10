n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite um segundo numero: '))
if n1 > n2:
    print('O maior numero é o {}'.format(n1))
elif n2>n1:
    print('O maior numero é o {}'.format(n2))
else:
    print('Os numeros sao iguais!')