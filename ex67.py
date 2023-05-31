while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n >= 0:
        print('-' * 20)
        cont = 1
        while cont <= 10:
            print(f'{n} x {cont} = {n * cont}')
            cont += 1
        print('-' * 20)
    if n < 0:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')