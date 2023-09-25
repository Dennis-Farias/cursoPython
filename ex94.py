pessoa = {}
listadepessoas = []
somaidade = mediaidade = 0
sexo = ''
while True:
    pessoa['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).upper()[0]
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F] ')).upper()[0]
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    resp = str(input('Quer continuar? [S/N] '))
    while resp not in 'SsNn':
        print('Erro! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] '))
    listadepessoas.append(pessoa.copy())
    if resp in 'Nn':
        break
mediaidade = somaidade / len(listadepessoas)
print('-=' * 30)
print(f'A) Ao todo temos {len(listadepessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {mediaidade:.2f} anos.')
print(f'C) As mulheres cadastradas foram ',end='')
for p in listadepessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ',end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in listadepessoas:
    if p['idade'] >= mediaidade:
        print('   ',end='')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<< ENCERRADO >>')
