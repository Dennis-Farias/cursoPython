n = int(input('Escolha o número que você quer saber a tabuada: '))
for c in range(0,11):
    print('{} x {} = {}'.format(n, c, n*c))