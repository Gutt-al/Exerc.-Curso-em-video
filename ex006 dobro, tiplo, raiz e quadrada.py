# ex006 Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada.

n = int(input('put a number:'))
do = (n*2)
tri = (n*3)
raiz = (n**(1/2))
print('your duplicate number and {}, your triplicate number and {},your number squared and {:2f}'.format(do, tri, raiz))