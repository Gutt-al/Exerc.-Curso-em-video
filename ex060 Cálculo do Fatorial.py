# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

import math

print('=X=x' * 7)
print('welcome to factorial!!!')
print('=X=x' * 7)
n = int(input('Type a number: '))
c = n
f = 1
# f = math.factorial(n)
print('calculating {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(' {}.'.format(f))
