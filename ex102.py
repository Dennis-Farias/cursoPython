def fatorial (num, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    '''
    print('-' * 30)
    if show == True:    
        fatorial = 1
        print(f'{num} ', end='')
        for c in range(num, 1, -1):
            fatorial *= c
            print(f'x {c-1} ',end='')
        return f'= {fatorial}'
    else:
        fatorial = 1
        for c in range(num, 0, -1):
            fatorial *= c
        return fatorial


print(fatorial(5, True))
help(fatorial)