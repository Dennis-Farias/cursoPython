ficha = {}
gol = []
totgol = 0
ficha['nome'] = str(input('Nome do Jogador: '))
qtpartidas = int(input('Quantas partidas {} jogou? '.format(ficha['nome'])))
for c in range(0, qtpartidas):
    gol.append(int(input('Quantos gols na partida {}? '.format(c+1))))
    totgol += gol[c]
ficha['gols'] = gol
ficha['total'] = totgol
print('-=' * 30)
print(ficha)
print('-=' * 30)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {ficha["nome"]} jogou {qtpartidas} partidas.')
for c in range(qtpartidas):
    print('    => Na partida {}, fez {} gols.'.format(c+1, gol[c]))
print(f'Foi um total de {totgol} gols.')