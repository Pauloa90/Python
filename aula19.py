filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}


locadora = list()
locadora.append(filme)


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



estado = dict()
pais = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    pais.append(estado.copy())
for e in pais:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
