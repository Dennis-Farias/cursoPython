print('-' * 30)
print('{: ^30}'.format(' LOJA SUPER BARATÃO '))
print('-' * 30)
totalcompra = maisde1000 = maisbarato = cont = 0
maisbaratoproduto = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = int(input('Preço: R$'))
    cont += 1
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        maisbaratoproduto = produto
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    totalcompra += preço
    if preço > 1000:
        maisde1000 += 1
    if op == 'N':
        break
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${totalcompra:.2f}')
print(f'Temos {maisde1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisbaratoproduto} que custa R${maisbarato:.2f}')