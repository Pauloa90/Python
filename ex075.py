a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
d = int(input('Digite um valor: '))
tupla = (a, b, c , d)

# Ou 
# tupla = (int(input('Digite um numero: )),
# int(input('Digite um numero: )),
# int(input('Digite um numero: )),
# int(input('Digite um numero: )),
# int(input('Digite um numero: )))

print(tupla)
print(f'O valor 9 apareceu na tupla {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O  primeiro valor 3 está na posicao de numero {tupla.index(3)}')
elif 3 not in tupla:
    print('O valor 3 nao foi encontrado dentro da tupla.')

print(f'Os numeros pares sao:', end='')

for x in tupla:
    if x % 2 == 0:
        par = x
        print(f'{par}')
        