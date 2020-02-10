num = int(input('Digite um numero inteiro: '))

print('''Escolha uma das opcoes para conversao:
[1] converter para Binario
[2] converter para Octal
[3] converter para Hexadecimal''')
option = int(input('Digite sua opcao: '))

if option == 1:
    print('O numero {} convertido para binario é {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('O numero {} convertido para Octal é {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('O numero {} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opcao Invalida!')