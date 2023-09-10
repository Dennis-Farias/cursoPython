maior = menor = 0
numeros = list()
for c in range(0, 5):
    numeros.append(int(input('Digite um valor para a posição {}: '.format(c))))
    if c == 0:
        maior = numeros[c]
        menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print('=-' * 30)
print('Você digitou os valores {}'.format(numeros))
print('O maior valor digitado foi {} nas posições '.format(maior), end='')
for i, v in enumerate(numeros):
    if v == maior:
        print('{}... '.format(i),end=''),
print()
print('O menor valor digitado foi {} nas posições '.format(menor), end='')
for i, v in enumerate(numeros):
    if v == menor:
        print('{}... '.format(i),end='')
print()
