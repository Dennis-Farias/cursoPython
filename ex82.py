numeros = []
numerospares = []
numerosimpares = []
resp = 'S'
while resp == 'S':
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        numerospares.append(num)
    else: 
        numerosimpares.append(num)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print('A lista completa é {}'.format(numeros))
print('A lista de pares é {}'.format(numerospares))
print('A lista de ímpares é {}'.format(numerosimpares))
