from random import randint

tupla = ()
for c in range(5):
    numero = randint(0,9)
    tupla += (numero,)
    if c == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print('Os valores sorteados foram: {}'.format(tupla))
print('O maior valor sorteado foi {}'.format(maior))
print('O menor valor sorteado foi {}'.format(menor))