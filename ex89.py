lista = []
nomes = []
notas = []
qt = 0
resp = 'S'
while resp == 'S':
    nomes.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    nomes.append(media[:])
    lista.append(nomes[:])
    qt += 1
    
print('-=' * 40)
print('No. NOME            MÉDIA')
print('-' *20)
for c in range(0, qt):
    print('{} {}          {}'.format(c, lista[c], nomes[c]))