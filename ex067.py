c = 0
n = 0
while True:
    n = int(input('Deseja ver a tabuada de que numero: '))
    c = 0
    while c < 10:
        print('-'*20)
        c += 1
        print(f'{n} x {c} = {n*c}')

        if n < 0:
            break