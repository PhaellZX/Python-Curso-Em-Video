# DESAFIO 16 #
# Crie um programa que leia um número real qualquer
# pelo teclado  e mostre na tela a sua posição inteira
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira é 6.

from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira é {}'.format(num,trunc(num)))

