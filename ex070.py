print('-'*20)
print('Vamos as compras!')
print('-'*20)

total = 0
p1000 = 0
menor = 0
c = 0
cheaper = ' '

while True:
    nome = str(input('O que deseja comprar: '))
    preco = float(input('Valor de produto : R$'))
    total += preco
    
    c += 1

    # Verificando quantos produtos acima de R$1000
    if preco > 1000:
        p1000 += 1

    # Verificando qual menor valor e qual produto mais barato
    if c == 1:
        menor = preco
        cheaper = nome
    else:
        if preco < menor:
            menor = preco
            cheaper = nome

    print('-'*20)   
    res = ' '
    while res not in 'SsNn':
        res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    print('-'*20)

    # Saindo do programa
    if res == 'N':
        break

print(f'O total gasto foi R${total:.2f}')
print(f'Temos {p1000} produtos que custam mais de R$1000.')
print(f'O produto mais barato é o {cheaper}.')