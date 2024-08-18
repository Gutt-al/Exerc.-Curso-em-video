# faça um programa que leia um numero de 0 a 9999
# e mostre na tela cada um dos digitos separados:
# ex: numero 1834
# unidade: 4 dezena: 3 centena: 8 milhar: 1

n = int(input('Type a number, n:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('The unidade and:{}'.format(u))
print('The dezena and:{}'.format(d))
print('the centena and:{}'.format(c))
print('the milhar and:{}'.format(m))
