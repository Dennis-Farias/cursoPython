sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
# ou, while sexo not in 'MF':
    sexo = str(input('Digite um sexo válido: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))