# EXERCICIO 11 #
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros
# quadrados. #

largura = float(input('Digite a largura da parede '))
altura = float(input('Digite a altura da parede '))

print('Sua parede tem a dimensão de {:.2f}X{:.2f} e sua area é de {:.3f}m²\nPara pintar essa parede, você precisará de {:.4f}L de tinta.'.format(largura,altura,(largura*altura),((largura*altura)/2)))