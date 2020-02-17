matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sumpares = 0
sumt = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            sumpares += matriz[l][c]
        sumt += matriz[l][2]
        if matriz[1][c] > maior:
            maior = matriz[1][c]

print('-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares digitados é {sumpares} ')
print(f'A soma dos numeros da terceira coluna é {sumt}')
# Or for l in range(0, 3):
#          sumt+= matriz[l][2]
print(f'O maior valor na segunda linha é o [{maior}]')