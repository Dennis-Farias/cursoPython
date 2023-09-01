qt9 = 0


num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais número: "))
num4 = int(input("Digite o último número: "))
tupla = (num1, num2, num3, num4)
if num1 == 9:
    qt9 += 1
if num2 == 9:
    qt9 += 1
if num3 == 9:
    qt9 += 1
if num4 == 9:
    qt9 += 1

if num1 == 3 or num2 == 3 or num3 == 3 or num4 ==3:
     pos3 = tupla.index(3)
else:
    pos3 = 0


if num1 % 2 == 0:
    numpares = num1
if num2 % 2 == 0:
    numpares = num2
if num3 % 2 == 0:
    numpares = num3
if num4 % 2 == 0:
    numpares = num4

print('Você digitou os valores {}'.format(tupla))
print('O valor 9 apareceu {} vezes'.format(qt9))
if pos3 == 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print('O valor 3 apareceu na {}ª posição'.format(pos3+1))
print('Os valores pares digitados foram {}'.format(numpares))