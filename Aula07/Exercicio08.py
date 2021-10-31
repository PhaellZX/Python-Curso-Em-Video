# EXERCICIO 08#

# Escreva um programa que leia uma valor em metros e convertar em km, hm, ...#

m = float(input('Digite uma distancia em metros: '))
print('A medida de {}m corresponde a\n{:.3f}km\n{:.2f}hm\n{:.1f}am\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(m,(m/1000),(m/100),(m/10),(m*10),(m*100),(m*1000)))