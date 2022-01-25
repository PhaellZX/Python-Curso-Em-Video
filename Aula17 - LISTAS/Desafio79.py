''' DESAFIO 79
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
'''
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor Adicionado com sucesso...')
    else:
        print('Valor Duplicado!')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break;
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
