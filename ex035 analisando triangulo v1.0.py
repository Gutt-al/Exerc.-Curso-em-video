# desenvolva um programa que leia o comprimento de tres retas
# e diga ao usuario se elas podem ou nao formar um triangulo
print('=-' * 200)
print('Triangle Analyzer!')
print('=-' * 200)

a = float(input('Type the first segment:'))
b = float(input('Type the secound segment:'))
c = float(input('Type the third segment:'))
r = a < b + c and b <a + c and c < a + b
if r:
    print('The segments above form a trangle!')
else:
    print('The segments above cannot form a triangle!')
