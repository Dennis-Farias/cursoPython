ficha = {}
ficha['Nome'] = str(input('Nome: '))
ficha['Média'] = float(input('Média: '))
if ficha['Média'] < 7:
    ficha['Situação'] = 'Reprovado'
else:
    ficha['Situação'] = 'Aprovado'
for k, v in ficha.items():
    print(f'{k} é igual a {v}')