''' DESAFIO 73
Exercício Python 073: Crie uma tupla preenchida com os
20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''

brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
               'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
               'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
               'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
posicao = 1
print('-=' * 5, end='')
print(' LISTA DE TIMES ',end='')
print('-=' * 5)
for time in brasileirao:
    print(f'{posicao} ° {time}')
    posicao += 1
print('-=' * 17)
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print('-=' * 17)
print(f'Os 4 últimos colocados são {brasileirao[-4:]}')
print('-=' * 17)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-=' * 17)
print(f'O Chapecoense está na {brasileirao.index("Chapecoense") + 1} posição')
