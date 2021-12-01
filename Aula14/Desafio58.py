# DESAFIO 58 #
# Melhore o jogo do DESAFIO 028 onde o computador
# vai "pensar" em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários
# para vencer.#

from random import randrange
print('-=-' * 20)
print('Vou pensar em número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
acertou = False
computador = randrange(0,11)
palpites = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        elif jogador > computador:
            print('Menos... tente mais uma vez')
print('PARABÉNS! Você conseguiu vencer! foi {} tentativas'.format(palpites))
