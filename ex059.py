n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
res = 0
print('0'*20)
while res != 5:
    res = int(input(''' O que deseja faze com os numeros {} e {}?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Numeros
    [5] Sair do programa\n'''.format(n1, n2)))
    if res == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif res == 2:
        print('A multiplicacao entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif res == 3:
        if n1 > n2:
            maior = n1
            print('O maior numero entre {} e {} é {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('O maior numero entre {} e {} é {}'.format(n1, n2, maior))
    elif res == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um segundo valor: '))
print('Programa concluido!')