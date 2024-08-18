# faça um programa que leia o nome da uma pessoa
# mostrando em seguida o primeiro
# nome e o ultimo nome separadamente

nome = str(input('Type your competed name:')).strip()
pn = nome.split()
print('Your completed name and:{}'.format(nome))
print('Your first name and?{}'.format(pn[0]))
print('Your last name and: {}'.format(pn[len(pn)-1]))
