# DESAFIO 19 #
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na
# tela o nome do escolhido.

from random import choice

aluno1 = input('Digite o primeiro aluno(a): ')
aluno2 = input('Digite o segundo aluno(a): ')
aluno3 = input('Digite o terceiro aluno(a): ')
aluno4 = input('Digite o primeiro aluno(a): ')

lista = [aluno1, aluno2, aluno3, aluno4]

print('O(A) aluno(a) escolhido(a) foi {}'.format(choice(lista)))