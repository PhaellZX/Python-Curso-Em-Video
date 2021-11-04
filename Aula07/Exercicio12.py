# EXERCICIO 12 #
# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preco do produto R$'))

print('Seu produto e R${:.2f} com 5% de desconto fica R${:.2f}'.format(preco,preco - (preco*5/100)))