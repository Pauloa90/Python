brasileiro = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Atletico-PR', 'Sao Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goias', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceara', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('-'*20)
print('O primeiros 5 colocados sao:')

for x in range(0, 5):
    print(brasileiro[x])

print('-'*20)
print('Os ultimos 4 colocados sao:')


print(brasileiro[-4:])

print('-'*20)
print('Em ordem alfabetica:')


print(sorted(brasileiro))


print(f'O Palmeiras está na posicao {brasileiro.index("Palmeiras")}')
