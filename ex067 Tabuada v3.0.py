# Faça um programa que mostre a tabuada de vários números
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

num = 0
while True:
    print('-*' * 25)
    num = int(input('Type a number for the multiplication table:'))
    print('-*' * 25)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')
print('Multiplication table closed until next time!')