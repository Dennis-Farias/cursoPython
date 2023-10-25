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