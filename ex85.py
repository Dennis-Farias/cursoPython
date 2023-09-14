numeros = []
numpares = []
numimpares = []
for c in range(1,8):
    num = int(input('Digite o {}o. valor: '.format(c)))
    if num % 2 == 0:
        numpares.append(num)
    else:
        numimpares.append(num)
numpares.sort()
numimpares.sort()
numeros.append(numpares[:])
numeros.append(numimpares[:])
print('-=' * 30)
print('Os valores pares digitados foram: {}'.format(numeros[0]))
print('Os valores ímpares digitados foram: {}'.format(numeros[1]))