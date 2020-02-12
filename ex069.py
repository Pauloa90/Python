print('-'*20)
print('Cadastro de Pessoas!')
print('-'*20)
totalpeople = 0
men = 0
women20 = 0
sexo =''

while True:
    idade = int(input('Digite a idade: '))
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo [M / F]: ')).strip().upper()[0]
    print('-'*20)
    res = str(input('Deseja continuar [S / N]: ')).strip().upper()[0]
    print('-'*20)
    if idade > 18:
        totalpeople += 1
    if sexo == 'M':
        men += 1
    if sexo == 'F' and idade < 20:
        women20 += 1
    if res == 'N':
        break
print(f'Foram cadastrados {totalpeople} pessoas com mais 18 anos')
print(f'Foram cadastrados {men} homens.')
print(f'Foram cadastradas {women20} mulheres com menos de 20 anos.')