def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    dicionario = {}
    soma = 0
    for c in range(len(num)):
        soma += num[c]
        if c == 0:
            maior = num[c]
            menor = num[c]
        else:
            if num[c] > maior:
                maior = num[c]
            if num[c] < menor:
                menor = num[c]
        media = soma / len(num)
    dicionario['total'] = len(num)
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['média'] = media
    if sit == True:
        if media >= 7:
            dicionario['situação'] = 'BOA'
        elif media < 7  and media >= 5:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario

    
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
help(notas)
