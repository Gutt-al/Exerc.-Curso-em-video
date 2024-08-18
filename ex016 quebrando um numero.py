# EX016 Crie um programa que leia um numero real qualquer
# pelo teclado e mostre na tela sua porção inteira:
# exemplo digite um numero: 6.127
# o numero 6.127 tem a parte inteira 6.
import math
num = float(input('Type a number:'))
r = math.trunc(num)
print('The whole number of {} and :{}'.format(num, r))
