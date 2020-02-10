ano = int(input('Digite o ano de nascimento: '))
idade = 2020 - ano

if idade < 9:
    print('Categoria Mirim')
elif idade > 9 and idade < 14:
    print('Categoria Infatil')
elif idade > 14 and idade < 19:
    print('Categoria Junior')
elif idade > 19 and idade < 25:
    print('Categoria Senior')
elif idade >= 25:
    print('Categoria MASTER')
