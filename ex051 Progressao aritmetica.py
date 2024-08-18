#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
#  mostre os 10 primeiros termos dessa progressão.

print('=+' * 25)
print('10 terms of an arithmetic progression (A.P)')
print('=+' * 25)
termo = int(input('Type first term'))
razao = int(input('Reason'))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c).format(decimo), end='→ ')
print('The end!')