'''
def soma(a, b):
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(2, 1)
'''
'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(b=4, a=5) #se eu colocar somente b=4, ele não vai entender que o a=5, então eu tenho que especificar os dois
soma(7, 2)
# soma(3, 9, 5), a quantidade de parâmetros tem que ser igual a pedida na função, então isso daria erro
'''
'''
def contador(*num): # o * ele não está informando quantos parâmetros vão ser passados, podem ser vários
    #print(num)
    for valor in num:
        print(f'{valor} ',end='')
    print('FIM!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''
'''
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)
'''