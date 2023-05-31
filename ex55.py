menor = 0
maior = 0
for c in range(1,6):
    peso = float(input('Peso da {}ª pessoa em kg: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso foi {} kg'.format(menor))
print('O maior peso foi {} kg'.format(maior))