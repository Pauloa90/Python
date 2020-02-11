s = 0
countf = 0
older = 0
nomev = ''
for x in range (0, 4):
    print('----{} Pessoa'.format(x))
    nome = str(input('Digite o nome:')).strip().upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o Sexo [M/F]: ')).strip().upper()
    s += idade
    if sexo == "M" and x == 0:
        older = idade
        nomev = nome
    if  sexo == "M" and idade > older:
            older = idade
            nomev = nome
    if sexo == "F":
        if idade < 20:
            countf += 1
mediaidade = s/4
print('O homem mais velho se chama {} e tem {} anos'.format(nomev, older))
print('A media da idade do grupo é {}'.format(mediaidade))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(countf))
