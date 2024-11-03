# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('___' * 10)
print('Lojas Gutt Tech')
print('___' * 10)
print('Welcome the Gutt Tech!')
total_c = 0
mais_caro = 0
menor = 0
cont = 0
while True:
    produto = str(input('Product name: ')).strip()
    preco = float(input('Price R$: '))
    cont = cont + 1
    total_c = total_c + preco
    if preco > 1000:
        mais_caro = mais_caro + 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Do you want to continue?[S/N]: ')).strip().upper()
    if opcao == 'N':
        break
print('{:-^40}'.format('Purchases completed'))
print(f'The Purchases were: {total_c:.2f}')
print(f'{mais_caro:.0f} produtc over R$:1,000. ')
print(f'The lowest priced product was a {produto} and it cost R$:{menor:.2}')
