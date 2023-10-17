def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    dicionario = {}
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['média'] = sum(num) / len(num)
    if sit == True:
        if dicionario['média'] >= 7:
            dicionario['situação'] = 'BOA'
        elif 7 > dicionario['média'] >= 5:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario

    
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)