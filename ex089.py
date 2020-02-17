aluno = list()
alunos = list()

while True:
    aluno.append(str(input('Digite o nome do Aluno: ')))
    aluno.append(float(input('Digite a primeira nota: ')))
    aluno.append(float(input('Digite a segunda nota: ')))
    
    media = (aluno[1]+aluno[2])/2
    aluno.append(media)
    alunos.append(aluno[:])
    aluno.clear()
    res = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if res in 'Nn':
        break

print('-='*10)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-='*10)

for i, l in enumerate(alunos):
    print(f'{i:<4}{l[0]:<10} {l[3]:>8.1f}')
while True:
    res = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if res == 999:
        break
    print(f'As notas de {alunos[res][0]} sao {alunos[res][1]} e {alunos[res][2]}')
print('Obrigado e Boa Sorte!')