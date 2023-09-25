from datetime import date
ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['nasc'] = int(input('Ano de Nascimento: '))
idade = date.today().year - ficha['nasc']
ficha['idade'] = idade
ficha['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if ficha['ctps'] != 0 and ficha['ctps'] > 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salário'] = float(input('Salário: R$ '))
    idadetrabalho = ficha['contratação'] - ficha['nasc']
    ficha['aposentadoria'] = idadetrabalho + 35
del ficha['nasc']
print('-=' * 30)
for k, v in ficha.items():
    print(f'  - {k} tem o valor {v}')
