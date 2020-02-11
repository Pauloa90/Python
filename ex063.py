print('-'*20)
print('Sequencia de Fibonacci')
print('-'*20)
n = int(input('Quantos termo voce quer mostrar: '))
t1 = 0
t2 = 1

print('-'*20)
print('{} - {}'.format(t1, t2), end='')

cont = 3
while cont <= n:
    cont += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(' - {}'.format(t3), end='')