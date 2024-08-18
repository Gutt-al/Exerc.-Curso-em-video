# Crie um programa que leia um numero inteiro
# e mostre na tela se ele e PAR ou IMPAR.

n = int(input('\033[0;33mType a number:'))
r = n % 2
if r == 1:
    print('this number {} is,\033[0;31modd'.format(n))
else:
    print('This number {} is, \033[0;34mEVEN'.format(n))
