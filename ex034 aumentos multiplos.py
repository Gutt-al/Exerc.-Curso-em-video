# Escreva um programa que pergunte o salario do funcionario
# e calcule o valor do seu aumento.
# igual ou maior que R$: 1.250,00 aumento  de 10%
# menores que R$: 1.250,00 aumento de 15%

s = float(input('What is your wage?'))
r = s + (s * 10 / 100)
r2 = s + (s * 15 / 100)
if s >= 1250:
    print('Your salary incresed to R$:{:.2f} '.format(r))
else:
    print('Your salary incresed to R$:{:.2f}'.format(r2))
