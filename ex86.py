matriz = []
for linha in range(3):
    for coluna in range(3):
        matriz.append(int(input('Digite um valor para [{}, {}]: '.format(linha, coluna))))
print('-=' * 30)
print(matriz)

