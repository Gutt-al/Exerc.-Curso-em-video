# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n1 = int(input("Enter a value: "))
n2 = int(input("Enter another value: "))
n3 = int(input("Enter another value: "))
n4 = int(input("Enter another value: "))
tupla = (n1, n2, n3, n4)
print(f"The numbers entered were: {tupla}")
print(f"The number 9 appeared {tupla.count(9)} Times!")
if 3 in tupla:
    print(f"The number 3 appeared in position {tupla.index(3) + 1}º")
else:
    print("The number 3 was not typed in any position!")
print("The even velues entered ware: ", end="")
for n in tupla:
    if n % 2 == 0:
        print(n, end=", ")
