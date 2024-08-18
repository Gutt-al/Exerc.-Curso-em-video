# Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time
print('Welcome to the Game Jo!...ken!...PÔ!')
print('''Choose one of the items: 
[ 0 ] Stone
[ 1 ] Paper
[ 2 ] scissors''')
items = ('Stone', 'Paper', 'Scissors')
pc = random.randint(0, 2)
jagador = int(input('Choose one:'))
print('~^~' * 11)
print('Jo!')
print('~^~' * 11)
time.sleep(1)
print('Ken!')
print('~^~' * 11)
time.sleep(1)
print('PÕ!!!')
time.sleep(0.8)
print('-=' * 11)
print('The pc choose {}'.format(items[pc]))
print('Player choose {}'.format(items[jagador]))
print('-=' * 11)
if pc == 0:
    if jagador == 0:
        print('\033[0;33mTie!\033[0;33m')
    elif jagador == 1:
        print('\033[0;32mYou win!!!\033[0;32m')
    elif jagador == 2:
        print('\033[0;31mYou Lose!\033[0;31m')
    else:
        print('invalid move')
elif pc == 1:
    if jagador == 0:
        print('\033[0;31mYou lose!\033[0;31m')
    elif jagador == 1:
        print('\033[0;33Tie!\033[0;33')
    elif jagador == 2:
        print('\033[0;32mYou win!!!!\033[0;32m')
    else:
        print('invalid move')
elif pc == 2:
    if jagador == 0:
        print('\033[0;32mYou win!!!\033[0;32m')
    elif jagador == 1:
        print('\033[0;31mYou lose\033[0;31m')
    elif jagador == 2:
        print('\033[0;33mTie!\033[0;33m')
    else:
        print('invalid move')
