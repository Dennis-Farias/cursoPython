'''
# docstrings
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Dennis Farias
    """
    c = i
    while c <= f:
        print(f'{c} ',end='')
        c += p
    print('FIM!')

help(contador)
'''
'''
# Argumentos opcionais
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
somar()
# como estou definindo os parametros = 0, eles vão ser opcionais, se eu chamar a função e colocar algum valor, ele vai receber, se não ele vai valer 0
# se eu chamar a função e passar mais valores do que tem de parametros ele vai dar erro
# poderia colocar que somente o parametro c = 0, então não seria necessário chamar a função passando 3 valores
'''
'''
# Escopo de variáveis
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

n = 2
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}')
# O n é uma variável global, então eu consigo acessar ela em qualquer parte do programa
# Já o x é uma variável local, pois ela está dentro de uma função, então eu só consigo acessar ela dentro da função, se eu tentar acessar fora, vai dar erro.
'''
'''
# Escopo de variáveis
def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
# ele vai criar uma variável global (a = 5) e uma variável local (a = 8)
# como (a = 5) está sendo pegado como parâmetro para b, ele vai pegar o valor de a e passar para b
'''
'''
# Escopo de variáveis
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
# como estou dentro da função estou definindo 'global a', a vai ser a = 8 tanto dentro como fora, local e global, ele vai valer fora o mesmo valor que dentro
# mas o b vai receber como parametro o a = 5
'''
'''
# Retorno de resultados
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')
'''