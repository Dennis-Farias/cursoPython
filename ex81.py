numeros = []
resp = 'S'
qtnumeros = 0
while resp == 'S':
    numeros.append(int(input('Digite um valor: ')))
    qtnumeros += 1
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print('Você digitou {} elementos.'.format(qtnumeros))
numeros.sort(reverse=True)
print('Os valores em ordem descrescente são {}'.format(numeros))
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
