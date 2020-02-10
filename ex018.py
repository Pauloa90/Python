import math
a = float(input('Digite o angulo que deseja saber o conseno e seno: '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tang = math.tan(math.radians(a))
print('Para o angulo {}, seu seno é {:.2f}, o seu cosseno é {:.2f} e sua tangente é {:.2f}.'.format(a, seno, cosseno, tang))
    