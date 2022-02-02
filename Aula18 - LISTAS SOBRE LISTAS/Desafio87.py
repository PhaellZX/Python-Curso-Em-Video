''' DESAFIO 87
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = [[0,0,0], [0,0,0], [0, 0, 0]]
soma = terceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor da posição da matriz[{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            terceira += matriz[l][c]
print()
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print('-=' * 30)
print(f'A soma de todos os valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')
