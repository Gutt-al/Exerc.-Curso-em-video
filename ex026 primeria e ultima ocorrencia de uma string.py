# faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes a parece um letra ''A''
# em que posição ela aparece a primeira vez
# em que posição ela aparece a ultima vez

frase = str(input('Type a sentence:')).strip()
x = frase.upper() . count('A')
pp = frase.upper() . find('A')+1
up = frase.upper() . rfind('A')+1
print('The letter appears {} something'.format(x))
print('The first letter A is in  position:{}'.format(pp))
print('The last letter A is in position:{}'.format(up))
