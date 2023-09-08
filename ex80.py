numeros = list()
for c in range(5):
    num = int(input('Digitd um valor: '))
    if c == 0:
        numeros.append(num)
        print('Valor adicionado ao final da lista...')
    if c == 1:
        if num < numeros[0]:
            print('Adicionado na posição 0 da lista...')
            numeros.insert(0, num)
        else:
            print('Valor adicionado ao final da lista...')
            numeros.append(num)
    if c == 2:
        if num > numeros[0] and num > numeros[1]:
            print('Valor adicionado ao final da lista...')
            numeros.append(num)
        elif num > numeros[0] and num < numeros[1]:
            print('Valor adicionado na posição 1 da lista...')
            numeros.insert(1, num)
        elif num > numeros[1] and num < numeros[0]:
            numeros.insert(1, num)
        else:
            print('Valor adicionado na posição 0 da lista')
            numeros.insert(0, num)
    
print('-=' * 30)
print('Os valores digitados em ordem foram {}'.format(numeros))