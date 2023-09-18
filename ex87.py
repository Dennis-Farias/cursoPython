matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somatercol = maiorseglin = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor para [{}, {}]: '.format(l, c)))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if c == 2:
            somatercol += matriz[l][c]
        if l == 1:
            if c == 0:
                maiorseglin = matriz[l][c]
            elif matriz[l][c] > maiorseglin:
                maiorseglin = matriz[l][c]
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print('[{:^5}] '.format(matriz[l][c]),end='')
    print()
print('-=' * 30)
print('A soma dos valores pares é {}.'.format(somapares))
print('A soma dos valores da terceira coluna é {}.'.format(somatercol))
print('O maior valor da segunda linha é {}.'.format(maiorseglin))