# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Type the {} value:'.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('The sum of {} numbers even, the values and {}'.format(cont, soma))
