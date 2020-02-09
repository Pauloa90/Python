import random
import time
alunos = ['Joao', 'Jessica', 'Paulo', 'Carol']
n = random.randint(1, 4)
print('Os alunos sao:')
for x in alunos:
    print(x)
print('Entre esses o sorteado foi:')
time.sleep(2)

print(alunos[n])