''' DESAFIO 96
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''
def area(largura,comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} X {comprimento} é de {a}m².')


# Programa principal
print(' Controle de Terreno')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)