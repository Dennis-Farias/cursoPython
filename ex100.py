from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(len(lista)):
        lista[c] = randint(1, 10)
        print(f'{lista[c]} ',end='', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    print(f'Somando os valores pares de {lista}, temos ',end='')
    somapar = 0
    for c in range(len(lista)):
        if lista[c] % 2 == 0:
            somapar += lista[c]
    print(somapar)

numeros = [0, 0, 0, 0, 0]
sorteia(numeros)
somaPar(numeros)