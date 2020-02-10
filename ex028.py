from random import randint
computador = randint(0, 5)
jogador = int(input('Em que numero eu pensei? '))
if jogador == computador:
    print('Parabens!')
else:
    print('Voce nao acertou!')