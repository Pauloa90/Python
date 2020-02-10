velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Multa! R${}'.format((velocidade-80) * 7))