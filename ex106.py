def manual():
    comando = ''
    while True:
        msg = 'SISTEMA DE AJUDA PyHELP'
        print('\033[0;30;43m~' * 30)
        print(f'{msg:^30}')
        print('~' * 30)
        comando = str(input('\033[mFunção ou Biblioteca > '))
        if comando == 'fim':
            print('\033[41m~~~~~~~~~~')
            print(' ATÉ LOGO!')
            print('~~~~~~~~~~\033[m')
            break
        print('\033[0;30;44m~' * 40)
        msg2 = f'Acessando o manual do comando {comando}'
        print(f'{msg2:^40}')
        print('~' * 40)
        print('\033[m')
        print(f'\033[7m')
        print(help(comando))
        print('\033[m')


manual()