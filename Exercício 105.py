dicionario = dict()


def notas(* notas, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a turma.
    """
    dicionario['total'] = len(notas)
    dicionario['maior'] = max(notas)
    dicionario['menor'] = min(notas)
    dicionario['média'] = sum(notas) / len(notas)
    if True:
        if dicionario['média'] <= 6:
            dicionario['situação'] = 'Ruin'
        elif 6 < dicionario['média'] < 8:
            dicionario['situação'] = 'Rasoável'
        else:
            dicionario['situação'] = 'Boa'
    return dicionario


notas(4.5, 10, 6.5)
print(f'{dicionario}')
help(notas)