# DESAFIO 18 #
# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

num = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(num))
cosseno = cos(radians(num))
tangente = tan(radians(num))

print('O ângulo de {:.2f} tem o SENO de {:.2f}\nO ângulo de {:.2f} tem o COSSENO de {:.2f}\nO ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(num,seno,num,cosseno,num,tangente))

