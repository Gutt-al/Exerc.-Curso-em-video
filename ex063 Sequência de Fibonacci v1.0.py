# Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-_' * 10)
print('Fibonacci Sequence')
print('-_' * 10)
termo = int(input('Whats are the terms you want? '))
cont = 3
t1 = 0
t2 = 1
t3 = t1 + t2
print('~~~~~~~' * termo)
print('{} -> {} -> '.format(t1, t2), end='')
while cont <= termo:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{} -> '.format(t3), end='')
    cont = cont + 1
print('END!!!')
print('~~~~~~~' * termo)
