pessoa = {}
listadepessoas = []
somaidade = mediaidade = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
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
print('- As mulheres cadastradas foram: ',end='')
for c in range(len(listadepessoas)):
    if listadepessoas[c]:
        c += 1
        if pessoa['sexo'] == 'F':
            print(f'{pessoa["nome"]} ',end='')
print()
print('- Lista das pessoas que estão acima da média: ')
for p in listadepessoas:
    if pessoa['idade'] > mediaidade:
        for k, v in pessoa.items():
            print()
            print(f'{k} = {v};')

print('<< ENCERRADO >>')
