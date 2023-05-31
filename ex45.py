from random import randint
itens = ('Papel', 'Pedra', 'Tesoura')
print('\033[1;34mVAMOS COMEÇAR O JOKENPÔ')
jogador = str(input('Escolha entre PAPEL, PEDRA e TESOURA: ')).capitalize()
n = randint(0, 2)
print('-=' * 11)
print('Computador jogou {}'.format(itens[n]))
print('Você jogou {}'.format(jogador))
print('-=' * 11)
if n == 0:
    computador = 'Papel'
elif n == 1:
    computador = 'Pedra'
elif n == 2:
    computador = 'Tesoura'
if jogador == 'Papel' and computador == 'Papel':
    print('\033[1;33mEMPATE!')
elif jogador == 'Tesoura' and computador == 'Papel':
    print('\033[1;32mVOCÊ GANHOU!')
elif jogador == 'Pedra' and computador == 'Papel':
    print('\033[1;31mVOCÊ PERDEU!')
elif jogador == 'Papel' and computador == 'Pedra':
    print('\033[1;32mVOCÊ GANHOU!')
elif jogador == 'Tesoura' and computador == 'Pedra':
    print('\033[1;31mVOCÊ PERDEU!')
elif jogador == 'Pedra' and computador == 'Pedra':
    print('\033[1;33mEMPATE!')
elif jogador == 'Papel' and computador == 'Tesoura':
    print('\033[1;31mVOCÊ PERDEU!')
elif jogador == 'Tesoura' and computador == 'Tesoura':
    print('\033[1;33mEMPATE!')
elif jogador == 'Pedra' and computador == 'Tesoura':
    print('\033[1;32mVOCÊ GANHOU!')
