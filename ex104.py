def leiaInt(num):
    print('-' * 30)
    n = str(input('Digite um número: '))
    while n not in '0123456789':
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        n = str(input('Digite um número: '))
    

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')