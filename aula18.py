'''
teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
# É necessário colocar o [:], para fazer uma cópia, se não ele vai criar uma ligação
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''
'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])
for p in galera:
    print('{} tem {} anos de idade.'.format(p[0], p[1]))
'''
galera = []
dado = []
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print('{} é maior de idade'.format(p[0]))
        totmai += 1
    else:
        print('{} é menor de idade'.format(p[0]))
        totmen += 1

print('Temos {} maiores e {} menores de idade.'.format(totmai, totmen))