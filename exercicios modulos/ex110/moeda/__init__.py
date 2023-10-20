def metade(n, form):
    n /= 2
    if form == True:
        n = f'R${n:.2f}'
    else:
        n = n
    return n

def dobro(n, form):
    n *= 2
    if form == True:
        n = f'R${n:.2f}'
    else:
        n = n
    return n 

def aumentar(n, porc, form):
    porc = n * (porc/100)
    n += porc
    if form == True:
        n = f'R${n:.2f}'
    else:
        n = n
    return n 

def diminuir(n, porc, form):
    porc = n * (porc/100)
    n -= porc
    if form == True:
        n = f'R${n:.2f}'
    else:
        n = n
    return n

def moeda(n):
    n = f'R${n:.2f}'
    return n

def resumo(n, porcaumento, porcredução):
    print('-' * 30)
    msg = 'RESUMO DO VALOR'
    print(f'{msg:^30}')
    print('-' * 30)
    print(f'Preço analisado:   {moeda(n)}')
    print(f'Dobro do preço:    {dobro(n, True)}')
    print(f'Metade do preço:   {metade(n, True)}')
    print(f'{porcaumento}% de aumento:    {aumentar(n, porcaumento, True)}')
    print(f'{porcredução}% de redução:    {diminuir(n, porcredução, True)}')