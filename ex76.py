a = 0
b = 1
tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 30)
print('{: ^30}'.format(' LISTAGEM DE PREÇOS '))
print('-' * 30)
while True:
    print('{}............R$  {:.2f}'.format(tupla[a], tupla[b]))
    a += 2
    b += 2
    if b-1 == len(tupla):
        break
print('-' * 30)
    


