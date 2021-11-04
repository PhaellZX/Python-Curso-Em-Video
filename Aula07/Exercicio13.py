# EXERCICIO 13 #
# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salario do funcionário R$'))

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,salario + (salario * 15/100)))