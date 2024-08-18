# Desenvolva um programa que pergunte a distancia de
# uma viagem em km. Calcule o preço da passagem
# cobrando  R$:0,50 por KH para viagens até 200km
# e R$:0,45 para viagens mais longas.

v = float(input('How many km is your trip?'))
v1 = v * 0.50
v2 = v * 0.45
if v <= 200:
    print('Your trip will cost, R$:{:.2f}'.format(v1))
else:
    print('Your trip will cost, R$:{:.2f}'.format(v2))
