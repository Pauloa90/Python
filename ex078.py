valores = []

maior = 0
menor = 0


for x in range (0,5):
    valores.append(int(input('Digite um valor : ')))

    if x == 0:
        maior = valores[x]
        menor = valores[x]
       
    else:
        if valores[x] > maior:
            maior = valores[x]
           
        if valores[x] < menor:
            menor = valores[x]
          
print('-'*30)
print(valores)
print(f'O maior valor encontrado foi o {maior} na posicao ', end=' ')
for x, v in enumerate(valores):
    if v == maior:
        print(f'{x}...', end='')
print(f'\nO menor valor encontrado foi o {menor} na posicao ', end=' ')
for x, v in enumerate(valores):
    if v == menor:
        print(f'{x}...', end='')
    
