salario = float(input('Digite o valor do seu salário: R$'))
if salario > 1250:
    print('O seu salário foi aumentado para \033[4;36mR${:.2f}'.format((salario*0.1)+salario))
else:
    print('O seu salário foi aumentado para \033[4;36mR${:.2f}'.format((salario*0.15)+salario))