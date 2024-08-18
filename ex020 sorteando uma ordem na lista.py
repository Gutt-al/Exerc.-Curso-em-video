# o mesmo professor do desafio anterior quer sorteaer a ordem
# de apresentação de trabalhos dos alunos
# faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.

import random

a1 = (input('type the name of student:'))
a2 = (input('tyoe the name of student:'))
a3 = (input('type the name of student:'))
a4 = (input('type the name of student:'))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('the order of names will be:{}'.format(lista))
