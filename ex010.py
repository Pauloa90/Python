reais = float(input('Quantos reais R$ voce tem na carteira: '))
dolar = reais / 3.27

print('Com R${:.2f} voce conseguirá comprar {:.2f} USD'.format(reais, dolar))