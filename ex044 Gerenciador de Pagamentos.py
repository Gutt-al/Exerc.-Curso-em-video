# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

import datetime

print('{:=^40}'.format(' Lojas Gutt '))

c = float(input('How much did you bui them?'))
print('''What is the payment method:
[ 1 ] Money or Pix: 10% of Discount
[ 2 ] Viem on card: 5% of discount
[ 3 ] 2x on card: normal value
[ 4 ] 3x or more on card: 20% of fees''')
opcao = int(input('what is the option? '))
pix = c * 10 / 100
cartao = c * 5 / 100
juros = c + (c * 20 / 100)
if opcao == 1:
    print('The value was: {:.2f} with 10% on the pix'.format(c - pix))
elif opcao == 2:
    print('The value was: {:.2f} with 5% on the cartão'.format(c - cartao))
elif opcao == 3:
    print('The value was 2x of:{:.2f}'.format(c / 2))
elif opcao == 4:
    p = int(input('How many installments?'))
    print('Will {} be installments of {:.2f},totalizing: {:.2f} '.format(p, juros / p, juros))
else:
    print('This option does not exist, choose one of the options above')
