# EXERCICIO 10 #
# Faça um programa que converta o valor em reais em dolar #

real = float(input('Quanto dinheiro você tem na carteira? R$'))
print("Com R${:.2f} você pode comprar US${:.2f}".format(real,(real / 5.64)))