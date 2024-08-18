# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=+' * 25)
print('10 terms of an arithmetic progression (A.P)')
print('=+' * 25)
termo = int(input('Type first term: '))
razao = int(input('Reason: '))
primeiro = termo
cont = 1
while cont <= 10:
    print('{}.'.format(primeiro), end='-> ')
    primeiro = primeiro + razao
    cont = cont + 1
print('THE END!!!')
