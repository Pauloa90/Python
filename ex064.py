s = 0
c = 0
contador = 0
# caso queria tirar a subtracao 999 basta adicionar antes do while
# c = int(input('Digite um numero: [999 para parar] '))

while c != 999:

    c = int(input('Digite um numero: [999 para parar] '))
    contador+= 1
    s+=c
print('O total de numeros digitados foi {}'.format(contador-1))
print('A soma dos numeros digitados foi {}'.format(s - 999))