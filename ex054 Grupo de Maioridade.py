# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

anos = datetime.date.today().year
totmaior = 0
totmenor = 0
print('majority group!')
for pess in range(1, 8):
    n = int(input('Type the year born of {}º person.'.format(pess)))
    idade = anos - n
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('in total, we have {} people of great'.format(totmaior))
print('and also {} people of minors!'.format(totmenor))