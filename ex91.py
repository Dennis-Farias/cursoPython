from random import randint
jogadores = {}
ranking = []
for c in range(4):
    jogadores['nome'] = 'jogador'
    jogadores['dado'] = randint(1,6)
    ranking.append(jogadores.copy())
print('Valore sorteados: ')
for v in jogadores.values():
    print(f'O {v} tirou {v}')
