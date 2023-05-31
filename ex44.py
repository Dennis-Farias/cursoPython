valor = float(input('Qual o preço do produto? R$ '))
forma = int(input('Selecione uma forma de pagamento: \n 1 - À vista no dinheiro/cheque (10% de desconto) '
'\n 2 - À vista no cartão (5% de desconto) \n 3 - Em até 2x no cartão (Preço normal) '
'\n 4 - 3x ou mais no cartão (20% de juros)\nQual é sua opção? '))
print(('Nosso sistema informa que: '))
if forma == 1:
    print('O novo preço do produto vai ser R$ {:.2f}'.format(valor - valor*0.1))
elif forma == 2:
    print('O novo preço do produto vai ser R$ {:.2f}'.format(valor - valor*0.05))
elif forma == 3:
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros'.format(valor/2))
    print('R$ {:.2f}'.format(valor))
elif forma == 4:
    parcelas = int(input('Quantas parcelas? '))
    novovalor = valor + valor * 0.2
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros'.format(parcelas, novovalor/parcelas))
    print('R$ {:.2f}'.format(novovalor))
else:
    print('\033[1;31mForma de pagamento inválida')
