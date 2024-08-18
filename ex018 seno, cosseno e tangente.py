# Faça um programa que leia um angulo
# qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

'''o python nao reconhece angulos, sempre que for usar tem que converter para radiano, Codigo: math.radians'''

import math

n = float(input('Type a angle:'))
seno = math.sin(math.radians(n))
co = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('of this entered angle the sine and: {:.2f}, the cosine  and: {:.2f}, the tangent and: {:.2f}'.format(seno, co, tan))
