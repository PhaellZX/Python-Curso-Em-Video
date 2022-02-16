''' DESAFIO 105
Faça um programa que tenha uma função notas() que pode
receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para
consulta pelo desenvolvedor.
'''
def notas(*notas, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param notas: uma ou mais notas dos Alunos (aceita várias)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionários com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['media'] = sum(notas)/len(notas)
    if situacao:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 1.5, situacao=True)
#print(resp)
help(notas)