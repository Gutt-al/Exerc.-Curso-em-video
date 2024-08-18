# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

import time

print('{||}' * 10)
print(' ')
print('prime dumber identifier: ')
print(' ')
print('{||}' * 10)
print(' ')
n = int(input('Type a number: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('{}'.format(c))
        tot = tot + 1
    else:
        print('{}'.format(c))
print('If the number is divisible by 3 or more, it is not prime')
time.sleep(3)
print('\033[0mO number {} was divisible by {}.\033[0m'.format(n, tot))
if tot == 2:
    print('\033[32mThats why hes cousin!\033[32m')
else:
    print('\033[31mthats why hes not a counsin!\033[31m')
    