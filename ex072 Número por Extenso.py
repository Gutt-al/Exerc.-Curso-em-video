#  Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso
#   de zero até vinte.
#  Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

import time

n_ex = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
        'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
        'Nineteen', 'Twenty')
contador = 0
while contador <= 20:
    print('If you enter a value greater than twenty the program will exit!')
    num = int(input('Write any number from 0 to 20 to show in full: '))
    if num > 20:
        break
    print(f'\033[0;31mYou typed the {n_ex[num]}\033[0;0m')
print('closing...')
print('-' * 20)
time.sleep(1.5)
print('Program closed!')
