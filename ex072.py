numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis' , 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = 0
while n >= 0 and n <= 20:
    
    n = int(input('Digite um numero entre 0 a 20: '))
    if n < 0 or n > 20:
        break
    print(numeros[n])
    res = ' '
    res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break


print('Obrigado, volte sempre!')
    