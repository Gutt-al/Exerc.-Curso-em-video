# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
# do salário ou então o empréstimo será negado.

pergunta = str(input('What is your objective with the loan?'))
casa = int(input('What the value of house?'))
anos = int(input('how many installments do you want?'))
salario = float(input('inform your salary:R$:'))
prestaçao = casa / anos
n1 = salario * 30 / 100
n2 = casa * 30 / 100
n3 = casa - n2
if prestaçao > n1:
    print('your request was danied,the installment was high!, must be below RS:{:.2f}'.format(n1))
else:
    print('Congratulations, your loan was approved! The installments were R$:{:.2f}'.format(prestaçao))
    print("The entrance value is: R$:{:.2f}".format(n2))
    print('The ')
print('Thank you, Have a good day!')
