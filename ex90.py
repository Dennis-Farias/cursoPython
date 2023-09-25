ficha = {}
ficha['Nome'] = str(input('Nome: '))
ficha['Média'] = float(input('Média: '))
print('-=' * 30)
if ficha['Média'] < 7 and ficha['Média'] >= 5:
    ficha['Situação'] = 'Recuperação'

elif ficha['Média'] < 5:
    ficha['Situação'] = 'Reprovado'

else:
    ficha['Situação'] = 'Aprovado'
for k, v in ficha.items():
    print(f'  - {k} é igual a {v}')