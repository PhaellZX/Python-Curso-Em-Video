# DESAFIO 29
#  Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
#  ele foi multado. A multa vai custar R$7,00 por cada Km acima
#  do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança! ')