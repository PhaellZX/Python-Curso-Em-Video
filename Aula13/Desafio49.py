# DESAFIO 49 #
#  Refaça o DESAFIO 009, mostrando a tabuada de um número
#  que o usuário escolher, só que agora utilizando um laço for.#

n = int(input('Digite um número: '))
print('-' * 12)
for cont in range(1,11):
    print('{} X {} = {:2}'.format(n,cont,(cont*n)))
print('-' * 12)