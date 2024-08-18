# Faça um programa que leia algo pelo teclado e
# mostre na tela o seu tipo
# primitivo e todas as informaçoes possiveis sobre ele.

a = input('Type something:')
print('The primitive type of this value and', type(a))
print('is it a number?', a.isnumeric())
print('is it numeric alpha?', a.isalnum())
print('is it alpha?', a.isalpha())