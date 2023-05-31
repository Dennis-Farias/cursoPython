from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
op = 0
while op != 5:
    op = int(input('''O QUE VOCÊ DESEJA FAZER?
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa
'''))
    if op == 1:
        print('A soma entre {} e {} é igual a {}'.format(n1,n2,n1+n2))
    elif op == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(n1,n2,n1*n2))
    elif op == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2,n1))
        else:
            print('Os valores são iguais')
    elif op == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print()
    sleep(2)
print('Fim do programa. Volte sempre!')