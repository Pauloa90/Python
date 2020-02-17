galera = [['joao', 30], ['pedro', 28], ['ana', 50]]
print(galera[0][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    print(galera)

for p in galera:
    if p[1] >= 21:
        
        print(f'{p[0]} é maior de idade com  {p[1]} anos')