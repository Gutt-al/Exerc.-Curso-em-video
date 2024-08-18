# crie um programa que leia um nome e diga se ela tem
# ''SILVA'' no nome

nome = str(input('Type your completed name:')).strip()
Snome = 'Silva' in nome
print('Your name {}, is has {}.'.format(nome, Snome))
