salario = float(input('Digite o seu salario: R$'))
casa = float(input('Digite o valor da casa: R$'))
tempo = int(input('Em quantos ano deseja pagar a casa: '))
presta = casa/(tempo * 12)
print('para pagar uma casa de R${} em {} anos a prestacao será de R${:.2f}'.format(casa, tempo, presta))

if presta > 0.3 * salario:
    print('Emprestimo negado!')
else:
    print('Emprestimo concedido!')