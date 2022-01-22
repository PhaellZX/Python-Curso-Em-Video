# Desafio 02 #
# Faça um programa que leia algo pelo #
# teclado e mostre na tela o seu tipo #
# primitivo e todas as informações possiveis #
# sobre ela #

var = input('Digite alguma coisa ')
print('É um número?') 
print(var.isnumeric())
print('É uma letra?')
print(var.isalpha())
print('Tem numero ou letra?')
print(var.isalnum())
