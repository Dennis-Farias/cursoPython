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