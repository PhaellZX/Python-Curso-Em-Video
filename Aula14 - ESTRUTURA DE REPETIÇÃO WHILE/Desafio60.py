''' DESAFIO 60
Faça um programa que leia um número qualquer
e mostre o seu fatorial.
'''

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! ||'.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))

# Usando o FOR

'''n = int(input('Digite um número para calcular seu fatorial: '))
f = 1
print('Calculando {}! ||'.format(n), end=' ')
for c in range(n, 0, -1):
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))'''
