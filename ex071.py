print('-'*20)
print('Banco Albuquerque')
print('-'*20)
notacinq = 0
notavinte = 0
notaum = 0
while True:
    valor = int(input('Quanto deseja sacar : R$ '))
    notacinq =  valor // 50
    notavinte = (valor % 50)//20
    notaum = (valor % 50) % 20
    print(f' O valor R${valor} será entregue em:')
    print(f'{notacinq} em notas de R$50')
    print(f'{notavinte} em notas de R$20')
    print(f'{notaum} em notas de R$1')
    res = ' '
    while res not in 'SsNn':
        res = str(input('Deseja continuar [S / N]')).strip().upper()[0]
    if res in 'Nn':
        break
    