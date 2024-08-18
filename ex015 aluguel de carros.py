# Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias
# pelas custas de R$60 por dia e R$:0.15 por km rodado

D = int(input('how many days will you rent the car? Days:'))
K = float(input('how many km driven: KM:'))
D1 = D*60.00
K1 = K*0.15
print('The total to be paid and: R$:{:.2f}'.format(D1 + K1))
