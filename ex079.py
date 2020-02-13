valores = []

while True:
    
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
    elif n in valores:
        print('O valor já foi encontrado nao lista! Ele nao será adicionado.')
   
    res = (str(input('Deseja contitnuar: [S/N]'))).strip().upper()[0]
    if res in 'Nn':
        break
print(sorted(valores))