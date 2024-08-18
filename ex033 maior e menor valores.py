# Faça um programa que leia tres numeros e
# mostre qual e o maior e qual e o menor.

a = int(input('First number:'))
b = int(input('Secound number:'))
c = int(input('third number:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('The smallest number and:{}'.format(menor))
print('The largest number and:{}'.format(maior))
