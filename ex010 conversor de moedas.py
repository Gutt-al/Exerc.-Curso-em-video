# ex010 Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('how much money do you have?'))
print('you with money {:.0f},you can buy {:.2f} dollars'.format(carteira, (carteira/5.1464)))