# DESAFIO 17 #
# Faça um programa qe leia o comprimento do cateto
# oposto e do cateto adjacente de triângulo retângulo,
# calcule e  mostre o comprimento da hipotenusa.#

from math import hypot
catOposto = float(input('Cateto Oposto: '))
catAdjacente = float(input('Cateto Adjacente: '))
print('O valor do cateto oposto é {}\n e do cateto adjacente é {}\n e a soma da hipotenusa e {}'.format(catOposto,catAdjacente,hypot(catOposto,catAdjacente)))