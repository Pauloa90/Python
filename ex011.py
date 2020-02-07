l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))
area = l * c
litros = area/2

print('Com a largura de {} e o comprimento de {} a area será de {}.'.format(l, c, area))
print('Para pintar uma area de {:.2f} será necessario {:.2f} litros de tinta.'.format(area, litros))