# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$200 R$100 R$50, R$20, R$10 e R$5.
import time

print('=' * 40)
print('{:^40}'.format('Banco Gutt'))
print('=' * 40)
print('Welcome Banco Gutt')
time.sleep(1)
print('We have the following notes: 5,10,20,50,100,200')
sac = int(input('How much do you want to withdraw? '))
total_sac = sac
ced = 200
tot_c = 0
while True:
    if total_sac >= ced:
        total_sac = total_sac - ced
        tot_c = tot_c + 1
    else:
        if tot_c > 0:
            print(f'The total of {tot_c} banknotes de R$: {ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        tot_c = 0
        if total_sac == 0:
            break
print('Always come back to Gutt Bank, have a good day!')
