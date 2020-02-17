grupo = [[], []]
for p in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        grupo[0].append(n)
    if n % 2 == 1:
        grupo[1].append(n)
print(f'A lista com numeros pares foi {sorted(grupo[0])}')
print(f'A lista com numeros impares foi {sorted(grupo[1])}')