tabela = ('Impressora', 350,'Tv', 1250, 'carro', 25000)

print('-'*40)
print(f'{"Listagem de Precos":^40}')
print('-'*40)

for x in range(0, len(tabela)):
    if x % 2 == 0:
        print(f'{tabela[x]:.<30}', end='')
    else:
        print(f'R${tabela[x]:>7.2f}')