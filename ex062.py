p = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razao da PA:  '))

c = 1
termo = p
question = 0
total = 0
question = 10

while question != 0:
    total += question
    while c < total:
        print('{} '.format(termo), end='')
        termo += r
        c += 1
        
    print('Pausa')
    question = int(input('Deseja ver mais quantos termos? '))
print('Fim')