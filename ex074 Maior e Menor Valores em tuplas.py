# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.

import random

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
n3 = random.randint(1, 100)
n4 = random.randint(1, 100)
n5 = random.randint(1, 100)
tupla = (n1, n2, n3, n4, n5)
print(f'List of generated numbers: {tupla}')
maior = max(tupla)
menor = min(tupla)
print(f"The largest number is: {maior}")
print(f"The smallest number is: {menor}")
