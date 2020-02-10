import random
import time

n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))

alunos = [n1, n2, n3, n4]
escolhido = random.choice(alunos)
print('O aluno escolhido foi: {}'.format(escolhido))
    