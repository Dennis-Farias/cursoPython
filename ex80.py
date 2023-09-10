numeros = list()
for c in range(5):
    num = int(input('Digitd um valor: '))
    if c == 0 or num >= numeros[len(numeros)-1]:
        numeros.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print('Adicionado na posição {} da lista...'.format(pos))
                break
            pos += 1
print('-=' * 30)
print('Os valores digitados em ordem foram {}'.format(numeros))