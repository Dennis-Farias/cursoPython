from random import randint
lista = [0, 0, 0, 0, 0]
def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(len(lista)):
        lista[c] = randint(1, 10)
        print(f'{lista[c]} ',end='')
    print('PRONTO!')

def somaPar(lista):
    print(f'Somando os valores pares de {lista}, temos ',end='')
    somapar = 0
    for c in range(len(lista)):
        if lista[c] % 2 == 0:
            somapar += lista[c]
    print(somapar)

sorteia(lista)
somaPar(lista)