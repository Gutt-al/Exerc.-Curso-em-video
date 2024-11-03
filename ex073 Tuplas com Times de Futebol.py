# Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense

import time

tabela = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Internacional', 'Bahia',
          'Cruzeiro', 'Atlético-MG', 'Vasco', 'Fluminense', 'Criciúma', 'Grêmio', 'Bragantino',
          'Juventude', 'Vitória', 'Corinthians', 'Athletico-PR', 'Cuiabá', 'Atlético-GO')
print('Welcome to the Brazilian championship table')
print(''' Options menu
To check the top 5 in the table, type { 1 }
to check the last 4 placed press { 2 }
to access the table in alphabetical order type { 3 }
to see what position Chapecoense's team is in, type { 4 }
to close type { 5 }''')
n = int(input("Enter the desired option: "))
while not n == 5:
    if n == 1:
        print(f"The top 5 teams are: {tabela[0:5]}")
    if n == 2:
        print(f"The last teams are: {tabela[16:21]}")
    if n == 3:
        print(f"{sorted(tabela)}")
    if n == 4:
        print('series B, { 15º } Chapecoense')
    n = int(input("Enter the desired option: "))
if n == 5:
    print("Closing Program...")
time.sleep(1.5)
print("Program Closed!")
