# DESAFIO 20 #
#  O mesmo professor do desafio 019 quer sortear a ordem de apresentação de
#  trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
#  e mostre a ordem sorteada.

from random import shuffle

aluno1 = input('Digite o primeiro aluno(a): ')
aluno2 = input('Digite o segundo aluno(a): ')
aluno3 = input('Digite o terceiro aluno(a): ')
aluno4 = input('Digite o primeiro aluno(a): ')

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print('A ordem de apresentação da lista é: ')
print(lista)