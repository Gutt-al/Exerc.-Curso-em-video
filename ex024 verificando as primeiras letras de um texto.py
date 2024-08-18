# faça um programa que leia o nome de uma
# cidade e diga se ela começa com ou não com
# o nome ''SANTO''

cid = str(input('Type a city:')).strip()
# nome = 'SANTO' in cid.upper() para achar o nome em qual quer possicão
# print('This city {} is has santo?{}'.format(cid, nome))
r = (cid[:5].upper() == 'SANTO')
print('This city is has santo?{}'.format(r))
