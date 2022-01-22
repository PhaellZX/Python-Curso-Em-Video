# DESAFIO 50 #
# Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar,
# desconsidere-o.#

soma = 0
pares = 0
for cont in range(1,7):
   num = int(input('Digite o {}° valor: '.format(cont)))
   if num % 2 == 0:
        soma += num
        pares += 1
print('Você digitou {} números PARES e a soma dos valores pares é de {}'.format(pares,soma))
