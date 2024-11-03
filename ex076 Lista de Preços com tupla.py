# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('-' * 50)
print(f'{"Price list!":^40}')
print('-' * 50)
tupla = ('Pencil', 1.75,
         'Eraser', 2.00,
         'Notebook', 15.90,
         'Pencil case', 25.00,
         'Backpack', 119.99,
         'Pen', 1.50,
         'Book', 34.90)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f"{tupla[pos]:.<30}", end=' ')
    else:
        print(f"R$:{tupla[pos]:>8.2f}")
print('-' * 50)
