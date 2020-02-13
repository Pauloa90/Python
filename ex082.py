lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    res = str(input('Quer continuar? {S/N}')).strip().upper()[0]
    if res in 'Nn':
        break
print(f'Minha lista completa é {lista}')
print(f'A lista com numeros pares: {pares}')
print(f'A lista com numeros impares: {impares}')