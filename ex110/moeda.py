def metade(n, form=False):
    n /= 2
    if form == True:
        n = moeda(n)
    else:
        n = n
    return n

def dobro(n, form=False):
    n *= 2
    if form == True:
        n = moeda(n)
    else:
        n = n
    return n 

def aumentar(n, porc, form=False):
    porc = n * (porc/100)
    n += porc
    if form == True:
        n = moeda(n)
    else:
        n = n
    return n 

def diminuir(n, porc, form=False):
    porc = n * (porc/100)
    n -= porc
    if form == True:
        n = moeda(n)
    else:
        n = n
    return n

def moeda(n):
    n = f'R${n:.2f}'.replace('.', ',')
    return n

def resumo(n=0, porcaumento=10, porcredução=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:   {moeda(n)}')
    print(f'Dobro do preço:    {dobro(n, True)}')
    print(f'Metade do preço:   {metade(n, True)}')
    print(f'{porcaumento}% de aumento:    {aumentar(n, porcaumento, True)}')
    print(f'{porcredução}% de redução:    {diminuir(n, porcredução, True)}')
    print('-' * 30)