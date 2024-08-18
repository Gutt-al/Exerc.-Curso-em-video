# Crie um programa que mostre na tela todos os
# números pares que estão no intervalo entre 1 e 50.

import time

n = str(input('What model number do you want to know, even or odd?'))
if n == 'even':
    for c in range(0, 100, 2):
        print(c)
        time.sleep(0.5)
    print('These are the even numbers!')
elif n == 'odd':
    for c in range(1, 100, 2):
        print(c)
        time.sleep(0.5)
    print('These are the odd numbers!')
else:
    print('Option invalid')
