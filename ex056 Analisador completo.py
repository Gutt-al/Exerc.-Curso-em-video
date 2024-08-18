# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher = 0
for pessoas in range(1, 5):
    print('{}º register!'.format(pessoas))
    nome = str(input('What your name? ')).strip()
    idade = int(input('how old are you?? '))
    sexo = str(input('What is your gender [M/F]? ')).strip().upper()
    somaidade = somaidade + idade
    if pessoas == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        mulher = mulher + 1
mediaidade = somaidade / 4
print('The middle de age is {:.2f}'.format(mediaidade))
print('The oldest is years old {} and his name is {}'.format(maioridadehomem, nomevelho))
print('In the group we have {} women, under 20 years old!'.format(mulher))
