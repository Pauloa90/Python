
n = 0
while True:
    n = int(input('Deseja ver a tabuada de que numero: '))
    if n < 0:
        break
    for c in range (1, 11):
        print('-'*20)
        print(f'{n} x {c} = {n*c}')
        

print('Volte sempre!')