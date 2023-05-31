from random import randint
from time import sleep
palpites = 1
computador = randint(0,10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print('-=-' *20)
sleep(1)
jogador = int(input('Em que número eu pensei? '))
sleep(1)
while computador != jogador:
    palpites = palpites + 1
    if jogador > computador:
        jogador = int(input('Errou! Você chutou acima do número que eu pensei. Tente novamente: '))
        sleep(1)
    elif jogador < computador:
        jogador = int(input('Errou! Você chutou abaixo do número que eu pensei. Tente novamente: '))
        sleep(1)
print('PARABÉNS! Você conseguiu me vencer!')
print('Você precisou de {} tentativas para ganhar!'.format(palpites))