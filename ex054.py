data = 2020
count = 0
menor = 0
for x in range(0, 6):
    ano = int(input('Qual o ano de nascimento: '))
    if  2020 - ano >= 18:
        count += 1
        
    else:
        menor += 1
print('{} ja atigiram a maioridade'.format(count))
print('{} nao antingiram a maioridade'.format(menor))

