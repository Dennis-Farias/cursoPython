numeros = []
c = 0
resp = 'S'
numeros.append(int(input('Digite um valor: ')))
print('Valor adicionado com sucessso...')
while resp == 'S':
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    numeros.append(int(input('Digite um valor: ')))
    if numeros[c] in numeros:
        print('Valor duplicado! Não vou adicionar...')
        numeros.pop()
        c += 1
    else:
        print('Valor adicionado com sucessso...')
print('-=' * 30)
print('Você digitou os valores {}'.format(sorted(numeros)))