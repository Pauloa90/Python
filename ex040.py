nota1 = float(input('Digite a primeita nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

if media < 5:
    print('Reprovado')
elif media >=ex065.py
 5 and media <= 6.9:
    print('Está em recuperacao')
elif media >= 7:
    print('Aprovado')
print(media)