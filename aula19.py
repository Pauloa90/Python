filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme['ano'])
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')
locadora = list()
locadora.append(filme)
print(locadora[0]['ano'])

for x in filme.keys():
    print(x)

for x in filme.values():
    print(x)

filme['titulo'] = 'A volta dos que nao foram'
print(filme)

filme['Peso'] = 102
print(filme)

# Criando dicionario dentro de uma lista!
brasil = list()
estado1 = {'uf': 'Pernambuco', 'sigla': 'PE'}
estado2 = {'uf': 'Rio de Janeiro', 'singla': 'RJ'}
estado3 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)