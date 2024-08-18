# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

import random

tentativas = 0
# acertou = False
jogador = ''
pc = random.randint(0, 10)
print('=*' * 20)
print('Welcome to the guessing game!')
print('=*' * 20)
print('Try to guess what number im thinking of!')
# while not acertou:
while pc != jogador:
    jogador = int(input('Whats your guess: '))
    tentativas = tentativas + 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('More... Try again!')
        elif jogador > pc:
            print('less... Try again!')
print('Congratulations, you win! attempts {}'.format(tentativas))
