''' DESAFIO 58
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos número
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma de {} + {} = {} '.format(n1,n2,(n1+n2)))
    elif opcao == 2:
        print('O resultado de {} X {} = {}'.format(n1,n2,(n1*n2)))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior é {} '.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('Entre {} e {} o maior é {} '.format(n1, n2, maior))
        else:
            print('Os números são iguais!!')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')