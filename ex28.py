import random
from time import sleep
n = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' *20)
p = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if p == n:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(n, p))

