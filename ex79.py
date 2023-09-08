numeros = []
resp = 'S'
while resp == 'S':
    num = int(input('Digite um valor: '))
    if num in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(num)
        print('Valor adicionado com sucessso...')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print('Você digitou os valores {}'.format(sorted(numeros)))