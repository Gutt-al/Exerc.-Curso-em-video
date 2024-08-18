# Escreve uma programa que converta uma temperatura digitada
# em ºC e converta ºF

C = float(input('how many degrees are you doing? ºC:'))
C1 = (C/5)*9
print('your degrees in ºF and:{:.1f}ºF'.format(C1+32))
