def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {area:.1f}m².')

print()
print('Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
