# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

p = int(input('Type the desired number:'))
print('''Choose one of the bases to convert:
[ 1 ] Conver to Binary.
[ 2 ] Conver to octal.
[ 3 ] Conver to hexadecimal.''')
o = int(input('Your option?'))
if o == 1:
    print('{} converted for binary end:{}'.format(p, bin(p)[2:]))
elif o == 2:
    print('{} converted for octal end:{}'.format(p, oct(p)[2:]))
elif o == 3:
    print('{} converted for hexadecimal end:{}'.format(p, hex(p)[2:]))
else:
    print('this option does not exist!')
