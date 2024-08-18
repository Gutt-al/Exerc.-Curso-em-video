# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

import random

print('-=' * 30)
print('Odd or Even Game!')
print('-=' * 30)
v = 0
while True:
    jogador = int(input('Type a value (1,10): '))
    pc = random.randint(0, 10)
    soma = jogador + pc
    escolha = str(input('What your choose? [O,E]')).strip().upper()
    print(f'You played {jogador}, The pc played {pc}, The total is {soma} ', end='')
    print('Even' if soma % 2 == 0 else 'Odd')
    print('-' * 60)
    if escolha == 'E':
        if soma % 2 == 0:
            print('You win!')
            v = v + 1
        else:
            break
    if escolha == 'O':
        if soma % 2 == 1:
            print('You win!')
            v = v + 1
        else:
            break
    print('Lest play again')
    print('-' * 60)
print(f'You loser!, Win {v} times')
