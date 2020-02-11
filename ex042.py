l1 = float(input('Digite o valor de um dos lados do triangulo: '))
l2 = float(input('Digite o valor de um dos lados do triangulo: '))
l3 = float(input('Digite o valor de um dos lados do triangulo: '))

# Conferindo possibilidade de ser triangulo
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    # conferindo equilatero:
    if l1 == l2 == l3:
        print('Triangulo Equilatero')
    elif l1 != l2 != l3 != l1:
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isosceles')
else:
    print('Nao foi possivel fazer um triangulo com os lados fornecidos: ')