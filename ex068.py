from random import randint


print('-'*20)
print('Vamos Jogar Par ou Impar!')
print('-'*20)

pc = randint(1, 10)
c = 0
v = 0
while True:
    n = int(input('Digite um numero: '))
    res = str(input('Par ou Impar [P/I] ')).strip().upper()[0]
    pc = randint(1, 10)   
    c += 1
    if res == 'P' and (pc + n) % 2 == 0:
        v += 1
        print('Voce ganhou! Jogue Novamente!')

    elif res == 'I' and (pc + n) % 2 == 1:
        v += 1
        print('Voce ganhou! Jogue Novamente!')

    elif res == 'P' and (pc + n) % 2 == 1:
        
        break
    elif res == 'I' and (pc + n) % 2 == 0:
        break
print(f'Voce perdeu! Venceu {v} vezes!')
