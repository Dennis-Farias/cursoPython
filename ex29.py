velocidade = float(input('Digite a velocidade que você estava: '))
limite = 80
if velocidade > limite:
    print('Você foi multado!')
    print('A multa foi de R${:.2f}'.format((velocidade-80)*7))
print('Tenha um bom dia! Dirija com segurança!')