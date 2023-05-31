cidade = str(input("Digite o nome da sua cidade: ")).strip()
dividido = cidade.split()
print('Santo' in dividido[0])
# outra forma de resolver
cidade = str(input("Digite o nome da sua cidade: ")).strip()
print(cidade[:5].upper() == 'SANTO')