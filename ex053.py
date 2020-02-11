pal = str(input('Digite para saber se é um Palindromo: ')).strip().upper()
pal = pal.replace(' ', '')
inverso = ''
for x in range(len(pal) -1, -1, -1):
    inverso += pal[x]
if inverso == pal:
    print('A frase {} é um palindromo!'.format(pal))
else:
    print('A frase {} nao e um palindromo'.format(pal))