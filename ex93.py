ficha = {}
gols = []
ficha['nome'] = str(input('Nome do Jogador: '))
qtpartidas = int(input('Quantas partidas {} jogou? '.format(ficha['nome'])))
for c in range(0, qtpartidas):
    gols.append(int(input('   Quantos gols na partida {}? '.format(c+1))))
ficha['gols'] = gols[:]
ficha['total'] = sum(gols)
print('-=' * 30)
print(ficha)
print('-=' * 30)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {ficha["nome"]} jogou {qtpartidas} partidas.')
for c in range(qtpartidas):
    print('   => Na partida {}, fez {} gols.'.format(c+1, gols[c]))
print(f'Foi um total de {ficha["total"]} gols.')