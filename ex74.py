from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: {}'.format(numeros))
print('O maior valor sorteado foi {}'.format(max(numeros)))
print('O menor valor sorteado foi {}'.format(min(numeros)))