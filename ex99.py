from time import sleep
def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for c in range(len(num)):
        print(f'{num[c]} ',end='')
        if c == 0:
            maior = num[c]
        else:
            if num[c] > maior:
                maior = num[c]
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        print('O maior valor informado foi 0.')
    else:
        print(f'O maior valor infomado foi {maior}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()