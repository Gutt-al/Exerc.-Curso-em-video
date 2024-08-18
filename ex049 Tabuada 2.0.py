# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input('which multiplication table do you want to know: '))
print('-=' * 10)
for c in range(1, 11):
    print('{} X {} = {}'.format(n, c, c * n))
print('-=' * 10)