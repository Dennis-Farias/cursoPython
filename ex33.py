a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and b < b:
    menor = c
print("O maior valor digitado foi \033[1;30;43m{}\033[m".format(maior))
print("O menor valor digitado foi \033[1;30;43m{}\033[m".format(menor))