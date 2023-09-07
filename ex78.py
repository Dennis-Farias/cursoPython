numeros = list()
for c in range(0, 5):
    numeros.append(int(input('Digite um valor para a posição {}: '.format(c))))

print('=-' * 30)
print('Você digitou os valores {}'.format(numeros))

for pos, num in enumerate(numeros):
    if pos == 0:
        maior = numeros[pos]
        menor = numeros[pos]
        posiçãomaior = pos
        posiçãomenor = pos
    else:
        if numeros[pos] >= maior:
            maior = numeros[pos]
            posiçãomaior = pos
        if numeros[pos] <= menor:
            menor = numeros[pos]    
            posiçãomenor = pos
print('O maior valor digitado foi {} nas posições {:.<4}'.format(maior, posiçãomaior))
print('O menor valor digitado foi {} nas posições {:.<4}'.format(menor, posiçãomenor))
