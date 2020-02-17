dic = dict()

dic['nome'] = str(input('Nome do aluno: '))
dic['media'] = float(input('Media do aluno: '))
if dic['media'] >= 7:
    dic['situacao'] = 'Aprovado'
elif 5 <= dic['media'] < 7:
    dic['situacao'] = 'Recuperacao'
else:
    dic['situacao'] = 'Repovado'
for k, v in dic.items():
    print(f'{k} é igual a {v}')