listajogadores = []
ficha = {}
gols = []
while True:
    print('-' * 30) 
    ficha['nome'] = str(input('Nome do Jogador: '))
    qtpartidas = int(input('Quantas partidas {} jogou? '.format(ficha['nome'])))
    for c in range(0, qtpartidas):
        gols.append(int(input('Quantos gols na partida {}? '.format(c+1))))
    ficha['gols'] = gols[:]
    ficha['total'] = sum(gols)
    listajogadores.append(ficha.copy())
    gols.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"cod":<5}{"nome":<10}{"gols":<10}{"total":>5}')
for c in range(len(listajogadores)):
    print(f'{c}   {listajogadores[c]["nome"]}     {listajogadores[c]["gols"]}         {listajogadores[c]["total"]}')
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if dados == 999:
        break
    if dados >= len(listajogadores):
        print(f'ERRO! Não existe jogador com código {dados}! Tente novamente')
        print('-' * 30)
        dados = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    print(f'-- LEVANTAMENTO DO JOGADOR {listajogadores[dados]["nome"]}:')
    for c in range(len(listajogadores[dados]['gols'])):
        print(f'   No jogo {c+1} fez {listajogadores[dados]["gols"][c]} gols.')
print('<< VOLTE SEMPRE >>')
