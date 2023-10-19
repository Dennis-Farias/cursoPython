def metade(n):
    n /= 2
    return n

def dobro(n):
    n *= 2
    return n 

def aumentar(n, porc):
    porc = n * (porc/100)
    n += porc
    return n 

def diminuir(n, porc):
    porc = n * (porc/100)
    n -= porc
    return n
