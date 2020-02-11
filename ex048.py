s = 0
cont = 0
print('Os numeros que sao impares, multiplos de 3 entre 1 - 500 sao:')
for x in range (0, 500):
    if x % 2 == 1 and x % 3 == 0:
        print(x)
        s +=x
        cont += 1
print('E o total é {}'.format(s))
print('Foram encontrados {} numeros que se enxcaixam nesse perfil'.format(cont))