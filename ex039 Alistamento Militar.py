# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai
# se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

print('lets see if you can enlist for military service now')
d = int(input('Type what year you were born:'))
ano = datetime.date.today().year - d
if ano > 18:
    print('You should have already enlisted.')
elif ano == 18:
    print('This year you must enlist!')
elif ano < 18:
    idade = 18 - ano
    print('its {} years before you enlist!'.format(idade))
