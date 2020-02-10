nome = str(input('Digite o seu nome: ')).strip()

print('Seu nome em MAIUSCULA é: {}'.format(nome.upper()))

print('Seu nome em MINUSCULA é: {}'.format(nome.lower()))

print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))

## print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()

print('Seu primeiro nome tem {} e ele tem {} letras'.format(separa[0], len(separa[0])))
