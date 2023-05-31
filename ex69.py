mais18 = homens = mulheresmenos20 = 0
while True:
    print('-' * 30)
    a = 'CADASTRE UMA PESSOA'
    print(f'{a: ^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' * 30)
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheresmenos20 += 1
    if op == 'N':
        break
b = ' FIM DO PROGRAMA '
print(f'{b:=^30}')
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheresmenos20} mulheres com menos de 20 anos')