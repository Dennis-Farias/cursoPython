viagem = float(input('Qual a distância da viagem em km? '))
if viagem <= 200:
    print('O preço da passagem vai ser R${:.2f}'.format(viagem*0.5))
else:
    print('O preço da passagem vai ser R${:.2f}'.format(viagem*0.45))