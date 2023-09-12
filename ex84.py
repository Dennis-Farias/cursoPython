galera = []
pessoas = []
maiorpeso = totpessoas = menorpeso = 0
resp = 'S'
while resp == 'S':
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    galera.append(pessoas[:])
    totpessoas += 1
    pessoas.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    for p in galera:
        if p[1] > maiorpeso:
            maiorpeso = p[1]
        if p[1] < menorpeso:
            menorpeso = p[1]
print('-=' * 30)
print('Ao todo você cadastrou {} pessoas.'.format(totpessoas))
print('O maior peso foi de {}Kg.'.format(maiorpeso))
print('O menor peso foi de {}Kg.'.format(menorpeso))
