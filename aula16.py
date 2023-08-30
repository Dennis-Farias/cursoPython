# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Tuplas são imutáveis
# lanche[1] = 'Refigerante'

# for comida in lanche:
#    print('Eu vou comer {}'.format(comida))

for cont in range(0, len(lanche)):
    print('Eu vou comer {} na posição {}'.format(lanche[cont], cont))

# for pos, comida in enumerate(lanche):
#    print('Eu vou comer {} na posição {}'.format(comida, pos))

# print('Comi pra caramba!')

# print(sorted(lanche))

# a = (2,5,4)
# b = (5,8,1,2)
# c = a + b
# print(c)
# print(c.count(5))
# print(c.index(5))
# cont = quantas vezes aparece, index é a posição que aparece

# print(c.index(5, 2))
# eu quero saber em qual posição está o 5, depois da 2 posição

# pessoa = ('Gustavo', 39, 'M', 99.88)
# print(pessoa)
# del(pessoa)
# para excluir uma tupla = del
# não se pode excluir determinado elemento em uma tupla, só ela inteira