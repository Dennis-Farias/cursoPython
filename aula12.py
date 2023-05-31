nome = str(input('Digite seu nome: '))
if nome == 'Dennis':
    print('Que nome bonito você tem')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Que nome normal você tem')
print('Tenha um bom dia, {}!'.format(nome))