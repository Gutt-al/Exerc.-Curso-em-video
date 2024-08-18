#  Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
#  mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa
#  deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

import time

opcao = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while opcao in 'S':
    n = int(input('Type a value: '))
    soma = soma + n
    quant = quant + 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Do you want to continue? [S/N]')).strip().upper()[0]
media = soma / quant
print('you type {} numbers, and averege was {}.'.format(quant, media))
time.sleep(0.8)
print('The biggest is {} and the smallest is {}.'.format(maior, menor))
print('finished program!!!')
