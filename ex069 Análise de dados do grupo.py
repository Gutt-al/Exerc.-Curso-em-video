# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

# mais de 18 anos
idcont = 0
# Homens cadastrados
homcont = 0
# Mulheres c menos de 20 anos
mucont = 0
while True:
    idade = int(input('How old are you? '))
    sexo = str(input('What is your sex [M/F]? ')).strip().upper()[0]
    sair = str(input('Do you want to exit [S/N]? ')).strip().upper()[0]
    if idade >= 18:
        idcont = idcont + 1
    if sexo == 'M':
        homcont = homcont + 1
    if sexo == 'F':
        if idade <= 20:
            mucont = mucont + 1
    if sair == 'S':
        break
print(f'There are {idcont} people over 18 years old. ')
print(f'{homcont} castrated men.')
print(f'{mucont} women under 20 years old.')

'''
# feito pelo professor

tot18 = 0
totH = 0
totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]? ')).strip().upper()[0]
    if idade >= 18:
        tot18 = tot18 + 1
    if sexo == 'M':
        totH = totH + 1
    if sexo == 'F' and idade < 20:
        totM20 = totM20 + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todos temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
'''