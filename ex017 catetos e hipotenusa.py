# Faça um programa que leia o comprimento
# do cateto oposto e do cateto adjacente de um triangulo
# retangulo, calcule e mostre o comprimento da hipotenusa.

# jeito 1
'''import math

Co = float(input('what is the opposite side:'))
Ca = float(input('what is the adjacent side:'))
calco = Co**2
calca = Ca**2
r = (calco + calca)
total = math.sqrt(r)
print('The hypotenuse and {:.2f}'.format(total) )'''

# jeito 2

'''Co = float(input('what is the opposite side:'))
Ca = float(input('what is the adjacent side:'))
hi = (Co ** 2 + Ca ** 2) ** (1/2)
print('The hypotenuse and {:.2f}'.format(hi))'''

# jeito 3

import math

Co = float(input('what is the opposite side:'))
Ca = float(input('what is the adjacent side:'))
hi = math.hypot(Co, Ca) # codigo da hipotenusa
print('The hypotenuse and {:.2f}'.format(hi))
