# Faça um programa que leia um ano qualqer e mostre se ele e bissexto.

import datetime

ano = int(input('what year do you want to analize? Type 0 to analyze the current year!'))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('The year {} is leap year!'.format(ano))
else:
    print('This year {} not is leap year!'.format(ano))
