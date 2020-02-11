contador = 0
total = 0
res = ''
maior = 0
menor = 0
while res != "N":
    n = int(input('Digite um valor: '))
    res = str(input('Deseja continuar? [s/n] ')).strip().upper()[0]
    contador += 1
    total += n
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = total/contador
print('A quantidade de numeros foi {}'.format(contador))
print('A media entre os numeros foi {:.2f}'.format(media))
print('O maior numero digitado foi {}'.format(maior))
print('O menor numero digitado foi {}'.format(menor))