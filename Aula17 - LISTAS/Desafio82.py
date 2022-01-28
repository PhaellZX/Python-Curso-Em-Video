''' DESAFIO 82
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente. Ao final, mostre
o conteúdo das três listas geradas.
'''
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'A lista completo é {num}')
print(f'A lista dos pares é {pares}')
print(f'A lista dos ímpares é {impares}')
