# um professor quer sortear um dos seus quatro alunos para apagar o quadro
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

a1 = (input('type the name of student:'))
a2 = (input('tyoe the name of student:'))
a3 = (input('type the name of student:'))
a4 = (input('type the name of student:'))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('The chosen student was:{}'.format(escolhido))
