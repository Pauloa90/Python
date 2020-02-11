maior = 0
menor = 0
for x in range(0, 5):
    peso = float(input('Digite o peso em Kg: '))
    if x == 0:
        maior = peso
        menor = peso 
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi Kg{}'.format(maior))
print('O menor peso lido foi Kg{}'.format(menor))