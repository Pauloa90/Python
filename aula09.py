frase = "Curso em VIdeo Python"
print(frase[9:21:2])


print(frase[15:])
print(frase[9::3])

print(len(frase))

print(frase.count('o', 0, 13))

print(frase.find('deo'))

print(frase.find('ola'))

print('Curso' in frase)

print(frase.replace('Python', 'Andoide'))

#frase.upper
print(frase.upper())

print(frase.lower())

print(frase.title())

print(frase.capitalize())

# Remove espacos
print(frase.strip())
# print(frase.rstrip())
# print(frase.lstrip())

# Dividir
frase = frase.split()
print(frase.split())

print('-'.join(frase))
