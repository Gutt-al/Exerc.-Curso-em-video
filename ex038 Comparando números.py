# Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = float(input('Type the number you want to compare:'))
n2 = float(input('Type the secound number you want to compare:'))
if n1 > n2:
    print('The first value is greater!')
elif n2 > n1:
    print('The secound value is greater!')
elif n1 == n2 or n2 == n1:
    print('Not exist value greater, both are equal!')
