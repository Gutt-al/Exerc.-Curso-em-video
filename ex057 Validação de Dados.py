# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

nome = str(input('Type your name: ')).strip().upper()
sexo = str(input('{}, what is your gender? [M/F]'.format(nome))).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Invalid gender, enter your correct gender, Please!: '.format(nome))).upper().strip()[0]
print('{} Successfully registered genre!'.format(sexo))
