from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    for c in range(inicio, fim, passo):
        print(f'{c} ', end='')
    print('FIM!')

contador(1,11,1)
contador(10,-1,-2)