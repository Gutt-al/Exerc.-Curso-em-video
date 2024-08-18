# crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as minusculas
# Quantas letras ao todo (sem considerar os espaços)
# quantas letras tem o primeiro nome

nome = str(input('Type your complete name:')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
# print('your first name has: {} numbers'.format(nome.find(' ')))
pn = (nome.split())
print('your first name and: {}, and has {} numbers'.format(pn[0], len(pn[0])))
# print('your first name has: {} numbers'.format(pn))
