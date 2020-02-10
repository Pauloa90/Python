km = float(input('Digite a quantidade de km percorrido com o carro alugado: '))
n = int(input('Digite a quantidade de dias que voce usou o carro: '))
valor = (60 * n) + (0.15 * km)
print('O preco calculado para {} dias e {}KM rodados é R${}.'.format(n, km, valor))
