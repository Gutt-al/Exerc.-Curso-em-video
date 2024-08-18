# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:

print('Palindrome detector!')
frase = str(input('Type a phrase:').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1): # Ultima letra, primeira letra, voltando
    inverso = inverso + junto[letra]
if inverso == junto:
    print('This is a Palindrome!')
    print(junto, inverso)
else:
    print('This is not a Palindrome')
    print(junto, inverso)
    print('they dont form the same sentence!')
