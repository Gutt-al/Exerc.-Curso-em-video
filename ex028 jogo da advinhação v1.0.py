# escreva um programa que faça o computador ''pensar'' em um numero interiro
# entre 0 e 5 peça para o usuario tentar descobrir qual foi o numero escolhido
# pelo computador. O programa deverá escrever na tela se o usuario venceu ou perdeu.

import random
import time

nome = str(input('Hello!My name is Rogerio the computer!\n What your name?'))
print('Welcome {}!'.format(nome))
a = str(input('{},shall we play a guessing game?'.format(nome)))
if a =='not':
    print('Ohh, okay... \n Have a good day!')
else:
    print('Very good, chosen a number from: 0 it is 5,If you pick the same number as me, you win!')
pc = random.randint(0, 5)
b = str(input('I chose mine, choose the your:'))
print('Loading...')
time.sleep(3)
if b == pc:
    print('You Win, chose the , congratulations')
else:
    print('You loser, I chose the {}, and you chose {}'.format(pc, b))
