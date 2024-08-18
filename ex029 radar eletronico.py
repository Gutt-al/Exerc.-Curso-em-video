# Escreva um programa que leia a velocidae de um carro
# se ele ultrapassar 80km/h. mostre uma mensagem dizendo
# que ele foi multado. A multa vai csutar R$: 7,00 por cada km
# acima do limite

import termcolor

v = int(input('What was the speed passed?'))
r = (v-80)*7
if v<=80:
    print('Okay, have a nice day, drive safely! ')
else:
    print('\033[0;31mYou received a mutation of R$:{:.2f}'.format(r))
