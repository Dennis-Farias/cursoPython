from random import randint
cont = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
while True:
    jogador = int(input('Diga um valor: '))
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    computador = randint(0,10)
    soma = jogador + computador
    if soma % 2 == 0:
        print('-' * 20)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
        print('-' * 20)
        if op == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 20)
            cont += 1
        if op == 'I':
            print('Você PERDEU!')
            print('-=' * 20)
            break
    if soma % 2 != 0:
        print('-' * 20)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        print('-' * 20)
        if op == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 20)
            cont += 1
        if op == 'P':
            print('Você PERDEU!')
            print('-=' * 20)
            break
print(f'GAME OVER! Você venceu {cont} vezes.')

