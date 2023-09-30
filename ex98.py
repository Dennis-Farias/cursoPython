from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo = -passo
    if passo == 0:
        passo += 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim < inicio:
        fim -= 1
        passo = -passo
    else:
        fim += 1   
    for c in range(inicio, fim, passo):
        print(f'{c} ', end='') 
    print('FIM!')

contador(1,10,1)
contador(10,0,2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)  
