something = input('Digite alguma coisa para ser avaliada: ')
print('O tipo primitivo desse valor é', type(something))
print('So tem espaco:', something.isspace())
print('É um numero: ', something.isnumeric())
print('É alfabetico: ', something.isalpha())
print('É alfanumerico:', something.isalnum())
print('Está maiscula ', something.isupper())
print('Está minuscula ', something.islower())
print('Está capitalizada ', something.istitle())