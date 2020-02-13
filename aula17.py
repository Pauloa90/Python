# LISTAS 
# lista.append('Elemento')
# lista.insert(0, 'Elemento')

# del.lista[3] 
# lista.pop(3) ou lista.pop() para eliminar o ultimo elemento da lista

#        veririfcar If 'elemento' in lista
# lista.remove('Elemento') lista.remove('Elemento')

valores = [2, 5, 1, 5]
valores[1] = 4
print(valores)

valores.append(9)
valores.sort(reverse=True)
print(valores)
print(f'Essa lista tem {len(valores)} elementos')

valores.insert(1, 0)
valores.remove(5)
valores.append(10)
print(valores)


if 10 in valores:
    valores.remove(10)
else:
    print('O valor 10 nao foi encontrado na lista')
print(valores)

lista = []
lista.append('a')
lista .append('b')
lista.append('c')

for posicao, valor in enumerate(lista):
    print(f'Na posicao {posicao} encontrei {valor} esse valor!')

tabela = []

for c in range (0, 5):
    tabela.append(int(input('Digite um valor: ')))
print(tabela)

for l, numero in enumerate(tabela):
    print(f'Encontrei o {numero} na posicao {l}')

a = [2, 3, 4, 6]
b = a[:]
b.append(10)
print(a, b)