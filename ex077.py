palavras = ('abeirou', 'abrunheiro', 'agricultores', 'aleijou', 'aleviou', 'amenizou', 'anuicoes', 'apicultores', 'apliquemos', 'aquecido', 'arqueiro', 'arquitecto', 'audicoes')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')