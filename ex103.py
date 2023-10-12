def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print('-' * 30)
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if nome != '' and gols != '': 
    print(ficha(nome, gols))
if nome == '' and gols == '':
    print(ficha())
if nome == '' and gols != '':
    print(ficha(nome='<desconhecido>', gols=gols))
if gols == '' and nome != '':
    print(ficha(nome))