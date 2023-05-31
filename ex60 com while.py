n = int(input('Qual o número você quer saber o fatorial? '))
mult = n
fatorial = n
while mult != 1:
    mult = mult - 1
    fatorial = fatorial * mult
print('O fatorial de {} é igual a {}'.format(n, fatorial))