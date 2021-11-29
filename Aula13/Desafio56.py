# DESAFIO 56 #
# Desenvolva um programa que leia o nome, idade e sexo
# de 4 pessoas. No final do programa, mostre: a média de
# idade do grupo, qual é o nome do homem mais velho e quantas
# mulheres têm menos de 20 anos.#

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeDoVelho = 0
totmulher20 = 0
for p in range(1,5):
    print('------ {}° PESSOA --------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeDoVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeDoVelho = nome
    if sexo in 'Mm' and idade < 20:
        totmulher20 += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem,nomeDoVelho))
print('Ao todo são {} mulheres com mais de 20'.format(totmulher20))