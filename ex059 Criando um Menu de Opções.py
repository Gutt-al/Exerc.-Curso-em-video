# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

import time

print('== +/-* ==' * 4)
print('Welcome to the calculations area ')
print('== +/-* ==' * 4)
n1 = float(input('Type a first number: '))
n2 = float(input('Type a second number: '))
opcao = 0
while opcao != 5:
    print(''' # Choose one of the options below!
    [ 1 ] Add
    [ 2 ] Multiplication
    [ 3 ] Bigger
    [ 4 ] New numbers
    [ 5 ] Exit the program''')
    opcao = int(input('Whats your option? '))
    if opcao == 1:
        print('adding...')
        time.sleep(1)
        print('The numbers {:.2f}, {:.2f} added = {:.2f}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('multiplying...')
        time.sleep(1)
        print('The numbers {:.2f}, {:.2f} multiplication = {:.2f} '.format(n1, n2, n1 * n2))
    elif opcao == 3:
        print('Analyzing...')
        time.sleep(1)
        if n1 == n2:
            print('These numbers are the same')
        elif n1 < n2:
            print('Of numbers {:.2f}, {:.2f}, the bigger and: {:.2f}'.format(n1, n2, n2))
        else:
            print('Of numbers {:.2f}, {:.2f}, the bigger and: {:.2f}'.format(n1, n2, n1))
    elif opcao == 4:
        print('choose again!')
        n1 = float(input('Type a first number: '))
        n2 = float(input('Type a second number: '))
    elif opcao == 5:
        print('Finishing...')
        time.sleep(1)
        print('Program closed, to the next!')

