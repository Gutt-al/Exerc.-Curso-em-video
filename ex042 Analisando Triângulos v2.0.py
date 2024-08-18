# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('\033[0;35m=-' * 50)
print('\033[0;30;0mAnalyzer Triangle')
print('\033[0;35m=-' * 50)

a = float(input('\033[0;30;0mType the first segment:'))
b = float(input('\033[0;30;0mType the secound segment:'))
c = float(input('\033[0;30;0mType the third segment:'))
r = a < b + c and b <a + c and c < a + b
if r:
    print('The segments above form a trangle,', end='')
    if a == b == c:
        print('equilateral!')
    elif a != b != c != a:
        print('scalene!')
    else:
        print('isoseles!')
else:
    print('The segments above cannot form a triangle!')
