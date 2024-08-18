# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

p = float(input('What is your weight? (KG) '))
a = float(input('What is your height? (M) ',))
r = p / (a ** 2)
print('The your IMC is:{:.1f}'.format(r))
if r < 18.5:
    print('You are underweight!')
elif 18.5 <= r < 25:
    print('You are at your ideal weight!')
elif 25 <= r < 30:
    print('You are overweight!')
elif 30 <= r <= 40:
    print('You are obese! be careful')
else:
    print('You are morbidly obese, you need to lose weight urgently!')
