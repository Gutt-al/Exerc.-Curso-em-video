# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('-*' * 10)
print('Welcome to values!!!')
print('-*' * 10)
n = 0
cont = 0
soma = 0
print('To finish, type [ 999 ]')
while n != 999:
    n = int(input('Type a value: '))
    cont = cont + 1
    soma = soma + n
    if n == 999:
        print('You typed {}, and the sum between them was {}.'.format(cont - 1, soma - 999))
print('To the next!!!')
