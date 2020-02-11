import time
print('Vamos estourar fogos em...')
for x in range (10, 0, -1):
    time.sleep(1)
    print('{}'.format(x))
print('FOGOS')