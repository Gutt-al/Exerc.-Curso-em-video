# A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

import time
import datetime

n = int(input('What year ware you born?'))
d = datetime.date.today().year
n1 = d - n
print('Checking your category...')
time.sleep(2)
print('You are {} years'.format(n1))
if n1 <= 9:
    print('you are in the category:Little')
elif n1 > 9 and n1 < 15:
    print('You are in the category:Infant')
elif n1 > 14 and n1 < 20:
    print('You are in the category:Junior')
elif n1 > 19 and n1 < 26:
    print('You are in the category:Senior')
elif n1 > 25:
    print('You are in the category:Master')
