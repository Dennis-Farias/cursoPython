frase = 'Curso em Vídeo Python'
#vai do 9º caractere até o 21º-1=20º
print(frase[9:21])
# o :2 no final pula de 2 em 2, do 9 para 11, 11 para 13
print(frase[9:21:2])
# vai do começo até o 5-1
print(frase[:5])
# vai do 15 até o final
print(frase[15:])
# começa do 9, vai até o final e pula de 3 em 3
print(frase[9::3])
# mostrar a quantidade de caracteres
print(len(frase))
# mostrar quantas vezes aparece um caractere
print(frase.count('o'))
# mostrar quantas vezes aparece o caractere entre alguns, sendo o último -1, ex:13-1
print(frase.count('o',0,13))
# onde se encontra o caractere ou os caracteres
print(frase.find('deo'))
# quando não existe os caracteres, aparece -1
print(frase.find('Android'))
# dizer se existe tals caracteres ou não
print('Curso' in frase)
# trocar palavras
print(frase.replace('Python','Android'))
# colocar tudo em maiúsculo
print(frase.upper())
# colocar tudo minúsculo
print(frase.lower())
# colocar a primeira letra em maiúsculo e o restante em minúsculo
print(frase.capitalize())
# a primeira letra de cada palavra ficar maiúsculo
print(frase.title())
teste = "   Aprenda Python  "
# retirar espaços inúteis no começo e no final da frase
print(teste.strip())
# retirar os espaços da direta
print(teste.rstrip())
# retirar os espaços da esquerda
print(teste.lstrip())
# dividir as palavras em listas, cada palavra vai representar uma lista, e dentro de cada lista a contagem começa do 0
# no parenteses do split, podemos colocar algum caractere que queremos que separe a partir dele, ex: split(/)
#ou a quantidade de vezes que queremos dividir, ex: split('/',2) ou split(none,2)
print(frase.split())
print(frase.split('o'))
print(frase.split('o',1))
# separar por algum caractere
print('-'.join(frase))
