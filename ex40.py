n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('\033[1;31mREPROVADO!')
elif media >= 7:
    print('\033[1;32mAPROVADO!')
else:
    print('\033[1;33mRECUPERAÇÃO!')