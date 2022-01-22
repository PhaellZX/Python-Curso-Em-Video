# DESAFIO 28
# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador. O programa deverá escrever na tela
# se o usuário venceu ou perdeu.#

from random import randrange
from time import sleep
print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
numero = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
computador = randrange(0,5)
if numero == computador:
    print('PARABÉNS! Você conseguiu vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador,numero))

