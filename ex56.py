idadetotal = 0
maisvelho = 0
menosvinte = 0
for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual o seu sexo [M/F]: ')).upper()
    idadetotal = idadetotal + idade
    if idade > maisvelho:
        if sexo == 'M':
            maisvelho = idade
            maisvelhonome = nome
    if idade < 20:
        if sexo == 'F':
            menosvinte = menosvinte + 1
print('A média de idade do grupo é de {} anos'.format(idadetotal/4))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(maisvelho, maisvelhonome))
print('{} mulher(es) tem menos de 20 anos'.format(menosvinte))