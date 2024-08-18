# ex011 Faça um programa que leia a largura e altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta
# pinta uma área de 2m quadrados.

L = float(input('What is the width of the wall?'))
A = float(input('What is the height of the wall?'))
R = L * A
print('your wall measurement is {}x{}, your wall has {:.3f}m²'.format(L, A, L*A))
tinta = R / 2
print('to paint this wall, you will need: {:.3f}L of paint'.format(tinta))
