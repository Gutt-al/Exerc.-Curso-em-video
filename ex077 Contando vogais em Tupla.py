# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

p1 = str(input("Type a Word: "))
p2 = str(input("Type Another Word: "))
p3 = str(input("Enter one more word: "))
p4 = str(input("Enter one more word: "))
p5 = str(input("Enter one more word: "))
tupla = (p1, p2, p3, p4, p5)
for p in tupla:
    print(f"\n In the word {p}, we have these vowels: ", end=' ')
    for v in p:
        if v.lower() in "aeiou":
            print(v, end=' ')
