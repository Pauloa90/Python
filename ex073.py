brasileiro = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Atletico-PR', 'Sao Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goias', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceara', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('O primeiros 5 colocados sao:')
print('-'*20)
for x in range(0, 5):
    print(brasileiro[x])

print('-'*20)
print('Os ultimos 4 colocados sao:')

print('-'*20)
print(brasileiro[-4:])

print('-'*20)
print('Em ordem alfabetica:')

print('-'*20)
print(sorted(brasileiro))

print('-'*20)
print(brasileiro.index('Palmeiras'))
