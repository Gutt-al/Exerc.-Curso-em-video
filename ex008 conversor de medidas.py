# ex008 escreva um programa que leia um valor em metros e o exiba
# convertido em centímetos e milímetros.

m = float(input('what distance do you want to caculate:'))
print('(decimetro) DM:{}'.format(m*10))
print('(centimetro) CM:{}'.format(m*100))
print('(milimetros) mm:{}'.format(m*1000))
print('(decametro) DM:{}'.format(m/10))
print('(hectometro) HM:{}'.format(m/100))
print('(quilometro) KM:{}'.format(m/100))