#  Faça um programa que mostre na tela uma contagem regressiva
#  para o estouro de fogos de artifício,
#  indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
import emoji
import pygame

print('Lets countdown to the new year!')
for c in range(10, - 1, -1):
    time.sleep(1)
    print(c)
print('🎉🎇🎆🎉🎇🎆🎉')
print('Happy New Year!')
pygame.init()
pygame.mixer.music.load('fogos.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
