''' DESAFIO 108
Adapte o código do desafio #107, criando uma função
adicional chamada moeda() que consiga mostrar os números
como um valor monetário formatado.
'''
import Moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.metade(p))}')
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.dobro(p))}')
print(f'Aumentando 10%, temos {Moeda.moeda(Moeda.aumentar(p, 10))}')
print(f'Diminuindo por 10% temos {Moeda.moeda(Moeda.diminuir(p, 10))}')