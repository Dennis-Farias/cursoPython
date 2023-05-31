casa = float(input('Qual o valor da casa que você quer comprar? R$ '))
salario = float(input('Qual o seu salário? R$ '))
tempo = int(input('Em quantos anos você quer pagar a casa? '))
prestacao = (casa/(tempo*12))
print('Para pegar uma casa de R$ {:.2f} em {} ano(s) a prestação será de R$ {:.2f} '.format(casa, tempo, prestacao))
if prestacao > (salario*0.3):
    print('Empréstimo negado')
else:
    print('Empréstimo concedido')