def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f'ERRO: \"{entrada}\" é um preco inválido!')
        else:
            valido = True
            return float(entrada)

