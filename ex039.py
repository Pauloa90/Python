ano = int(input('Digite o ano de nascimento: '))
idade = 2020 - ano
# Ainda vai se alistar
if idade < 18:
    print('Voce tem {} anos. deverá se alistar em {} anos'.format(idade, 18 - idade))
# Hora de se alistar
elif idade == 18:
    print('Voce com {} anos deve se alistar imediatamente.'.format(idade))
# Passou do tempo de se alistar
else:
    print('Voce deveria se alistar {} anos atras caso nao o tenha feito'.format(idade -18))