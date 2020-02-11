p = float(input('Qual o preco do produto R$: '))
op = int(input(''' Escolha a opcao de pagamento:
[ 1 ] A vista dinheiro/cheque
[ 2 ] A vista no cartao
[ 3 ] em até 2x no cartao
[ 4 ] 3x ou mais no cartao '''))

if op == 1:
    print('Voce ganhou 10% \de desconto. Preco normal R${:.2f} e com desconto R${:.2f}'.format(p, p * 0.9))
elif op == 2:
    print('Voce terá 5%\ de descopnto. Preco normal R${:.2f} e com desconto R${:.2f}'.format(p, p * 0.95))
elif op == 3:
    print('Voce nao tera desconto pagando em 2x no cartao. Valor total R${}'.format(p))
elif op == 4:
    print('Em 3x no cartao existe um juros de 20%\. Preco normal R${} e a pagar R${}'.format(p, p * 1.2))