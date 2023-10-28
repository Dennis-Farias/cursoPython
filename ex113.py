def leiaInt(msg):
    try:
        ok = False
        valor = 0
        while True:
            n = str(input(msg))
            if n.isnumeric():
                valor = int(n)
                ok = True
            else:
                print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            if ok:
                break
        return valor
    except KeyboardInterrupt:
        print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
        return 0

def leiaFloat(msg):
    try:
        ok = False
        valor = 0
        while True:
            n = str(input(msg))
            if n.replace('.', '', 1).isdigit():
                valor = float(n)
                ok = True
            else:
                print('\033[0;31mERRO: por favor, digite um número real válido.\033[m')
            if ok:
                break
        return valor
    except KeyboardInterrupt:
        print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
        return 0
    

inteiro = leiaInt('Digite um Inteiro: ') 
real = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')