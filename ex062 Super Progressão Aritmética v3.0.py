# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('=+' * 25)
print('10 terms of an arithmetic progression (A.P)')
print('=+' * 25)
primeiro = int(input('Type first term: '))
razao = int(input('Reason: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}.'.format(termo), end='-> ')
        termo = termo + razao
        cont = cont + 1
    print('Pause...')
    mais = int(input('How many more terms do you want to show: '))
print('Progression completed with {} more terms!'.format(total))
