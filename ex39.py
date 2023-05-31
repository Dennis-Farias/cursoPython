from datetime import date
sexo = int(input('''Qual é o seu sexo?
1 - MASCULINO
2- FEMININO
Sua opção: '''))
if sexo == 2:
    print('Você não precisa fazer alistamento militar')
elif sexo == 1:
    ano = int(input('Digite o seu ano de nascimento: '))
    idade = date.today().year - ano
    if idade < 18:
        saldo = 18 - idade
        print('Você ainda vai se alistar ao serviço militar')
        print('Faltam {} ano(s) para você poder se alistar'.format(saldo))
        print('Seu alistamento será em {}'.format(date.today().year + saldo))
    elif idade == 18:
        print('Já está na hora de se alistar no serviço militar')
    else:
        saldo = idade - 18
        print('Você já passou do tempo de se alistar no serviço militar')
        print('Você passou {} ano(s) do prazo'.format(saldo))
        print('Seu alistamento foi em {}'.format(date.today().year - saldo))
