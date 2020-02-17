pessoa = dict()
grupo = list()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')

    pessoa['idade'] = int(input('Digite a idade: '))
    grupo.append(pessoa.copy())
    res = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    while res not in 'SsNn':
            res = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if res == 'N':
        break
print(pessoa)