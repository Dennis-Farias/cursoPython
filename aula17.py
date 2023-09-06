# num = [2,5,9,1]
# num[2] = 3
# num.append(7)
# append serve para adicionar um item no final da lista
# num.sort(), serve para colocar em ordem
# num.sort(reverse=True)
# serve para colocar na ordem contrária
# num.insert(2, 0)
# serve para colocar o 0 na 2ª posição
# num.pop() remove o último elemento
# num.pop(4) remove o elemento que está na 4ª posição 
# num.remove(2) remove o número 2, mas somente na primeira vez que ele aparece
#if 4 in num:
#    num.remove(4)
#else:
#    print('Não achei o número 4')
# print(num)
# print('Essa lista tem {} elementos'.format(len(num)))

'''
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print('Na posição {} encontrei o valor {}!'.format(c, v))
print('Cheguei ao final da lista.')
# vai pegar a posição e o valor
'''

a = [2,3,4,7]
b = a
b[2] = 8
# b = a, vai fazer uma ligação entre as duas variaveis, o que alterar em b também vai ser alterado em a
# para criar uma copia, onde se alterar em um, não vai mexer no outro, use o comando: b = a[:]
print('Lista A: {}'.format(a))
print('Lista B: {}'.format(b))
