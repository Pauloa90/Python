from time import sleep
from random import randint

sleep(1)
print('-'*20)
sleep(0.3)
print('JoKenPo!')
sleep(0.3)
print('-'*20)

op = int(input('''Vamos jogar Pedra, Papel e Tesoura:
[1] Papel
[2] Pedra
[3] Tesoura \n'''))

pc = randint(1, 3)
if op == pc:
     print('Empate! Jogue novamente!')
elif op == 1 and pc == 2:
    print('Voce ganhou, papel cobre pedra!')
elif op == 1 and pc == 3:
    print('Voce perdeu! Tesoura corta o papel!')
elif op == 2 and pc == 1:
    print('Voce perdeu! Papel cobre pedra!')
elif op == 2 and pc == 3:
    print(' Voce ganhou! Pedra quebra tesoura!')
elif op == 3 and pc == 1:
    print(' Voce ganhou! Tesoura corta papel!')
elif op == 3 and pc == 2:
     print(' Voce perdeu! Pedra quebra tesoura!')
print('Jogue novamente!')