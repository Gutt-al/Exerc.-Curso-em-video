# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
n = 0
soma = 0
cont = 0
while True:
    n = int(input('Type a number (999 to stop!):'))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f'The sum of the {cont} values are: {soma}')
