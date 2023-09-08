aberto = False
fechamento = False
expressao = str(input('Digite a expressão: '))
for c in range(len(expressao)):
    abertura = expressao[c]
    if abertura == '(':
        aberto = True
        c += 1
    elif abertura == ')':
        if aberto == False:
            print('Sua expressão está errada!')
        else:
            print('Sua expressão está válida!')
            fechamento = True
            c += 1
if aberto == True and fechamento == False:
    print('Sua expressão está errada!')
elif fechamento == False:
    print('Sua expressão está errada!')
    
