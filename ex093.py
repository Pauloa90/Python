jogador = dict()
partidas = list()
sum = 0
jogador['nome'] = str(input('Digite o nome do Jogador: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for x in range(0, n):
    partidas.append(int(input(f'Quantos gols na partida {x+1}? ')))



jogador['gols'] = partidas
for x in jogador['gols']:
    sum += x
print(jogador)
print(sum)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')