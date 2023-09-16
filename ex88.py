from random import randint
from time import sleep
jogos = []
bilhete = []
print('-' * 30)
print('{: ^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
numjogos = int(input('Quantos jogos você quer que eu sorteie? '))
while len(jogos) < numjogos:
    while len(bilhete) < 6:
        numeros = randint(1,60)
        if numeros not in bilhete:
            bilhete.append(numeros)
    bilhete.sort()
    jogos.append(bilhete[:])
    bilhete.clear()
print('{:=^30}'.format(' SORTEANDO {} JOGOS ').format(numjogos))
for c in range(0, len(jogos)):
    print('Jogo {}: {}'.format(c+1, jogos[c]))
    sleep(1)
print('{:-^30}'.format(' < BOA SORTE! > '))