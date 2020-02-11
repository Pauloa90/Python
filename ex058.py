import random
computador = 0


user = int(input('Digite um numero inteiro e tente adivinhar o numero que o computador pensou de 0 a 5: '))
while computador != user:
    computador = random.randint(0, 5)

    user = int(input('Voce perdeu, digite novamente para tentar acertar!'))
print('Acertou voces pensaram no {}'.format(computador))