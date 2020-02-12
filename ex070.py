print('-'*20)
print('Vamos as compras!')
print('-'*20)
total = 0
p1000 = 0
res = ''

cheaper = ''

while True:
    nome = str(input('O que deseja comprar: '))
    preco = float(input('Valor de produto : R$'))
    menor = preco
    print('-'*20)
    res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    print('-'*20)

    total += preco
    if preco < menor:
        cheaper = nome

    if preco > 1000:
        p1000 += 1

    if res == 'N':
        break

print(f'O total gasto foi R${total:.2f}')
print(f'Temos {p1000} produtos que custam mais de R$1000.')
print(f'O produto mais barato é o {cheaper}.')