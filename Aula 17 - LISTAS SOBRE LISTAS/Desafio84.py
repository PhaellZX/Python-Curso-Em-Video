''' DESAFIO 84
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
temp = list()
princ = list()
pesados = leves = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        pesados = leves = temp[1]
    else:
        if temp[1] > pesados:
            pesados = temp[1]
        elif temp[1] < leves:
            leves = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {pesados}Kg, Peso de ', end=' ')
for p in princ:
    if p[1] == pesados:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {leves}Kg, Peso de ', end=' ')
for m in princ:
    if m[1] == leves:
        print(f'[{m[0]}]', end=' ')
print()

