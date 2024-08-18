#  Crie um programa que leia duas notas de um aluno e calcule sua média,
#  mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input('Type your note:'))
n2 = float(input('Type your note:'))
media = (n1 + n2) / 2
print('taking {} is {}, the average will be:{}'.format(n1, n2, media))
if media >= 5 and media < 7:
    print('You ate average, study more to improve your average!')
elif media >= 7:
    print('Congratulation, you are great keep it up!')
elif media < 5:
    print('are you recovering!')
