listajogadores = []
ficha = {}
gols = []
while True:
    print('-' * 50) 
    ficha['nome'] = str(input('Nome do Jogador: '))
    qtpartidas = int(input('Quantas partidas {} jogou? '.format(ficha['nome'])))
    for c in range(0, qtpartidas):
        gols.append(int(input('  Quantos gols na partida {}? '.format(c+1))))
    ficha['gols'] = gols[:]
    ficha['total'] = sum(gols)
    listajogadores.append(ficha.copy())
    gols.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"cod":<5}{"nome":<15}{"gols":<15}{"total":>5}')
for c in range(len(listajogadores)):
    print(f'{c:<5}{str(listajogadores[c]["nome"]):<15}{str(listajogadores[c]["gols"]):<15}{str(listajogadores[c]["total"]):>5}')
while True:
    while True:
        print('-' * 50)
        dados = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
        if dados == 999:
            break
        if dados < len(listajogadores):
            break
        print(f'ERRO! Não existe jogador com código {dados}! Tente novamente!')
    if dados == 999:
            break
    print(f'-- LEVANTAMENTO DO JOGADOR {listajogadores[dados]["nome"]}:')
    for c in range(len(listajogadores[dados]['gols'])):
        print(f'   No jogo {c+1} fez {listajogadores[dados]["gols"][c]} gols.')
print('<< VOLTE SEMPRE >>')
