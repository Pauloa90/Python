lista = []

while True:
    n = int(input('Digite um numero: '))
    res = ' '
    lista.append(n)
    while res not in 'SsNn':
        res = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if res in 'Nn':
        break

lista.sort(reverse=True)
print(f'Foram encontrados {len(lista)} numeros na lista.')
print(f'A lista em ordem descrescente é: {lista}')

if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else: 
    print('O valor 5 nao foi encontrado na lista.')
