pessoa = {}
listadepessoas = []
somaidade = mediaidade = 0
mulheres = []
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    resp = str(input('Quer continuar? [S/N] '))
    listadepessoas.append(pessoa.copy())
    if resp in 'Nn':
        break
mediaidade = somaidade / len(listadepessoas)
print('-=' * 30)
print(f'- O grupo tem {len(listadepessoas)} pessoas.')
print(f'- A média de idade é de {mediaidade:.2f} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}')
print('- Lista das pessoas que estão acima da média: ')
for p in listadepessoas:
    print()
    if pessoa['idade'] > mediaidade:
        for k, v in pessoa.items():
            print(f'{k} = {v}; ',end='')
print()
print('<< ENCERRADO >>')
