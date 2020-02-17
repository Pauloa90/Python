dados = list()
grupo = list()
n = 0
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    grupo.append(dados[:])
    n += 1
    dados.clear()
    res = str(input('Deseja continuar? [S / N]')).strip().upper()[0]
    if res in 'Nn':
        break
    
print(f'No total foram cadastradas {n} pessoas', end='')
print(f'O maior peso foi {maior} kg')
for p in grupo:
    if p[1] == maior:
        print(f'{p[0]} ', end='')

print(f'O menor peso cadastrado foi {menor} de ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'{p[0]} ')


