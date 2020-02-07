preco = float(input('Digite o valor do produto: '))
desconto = preco/100*5
print('O valor do produto na promocao será de R${:.2f}.'.format(preco - desconto))
