n = int(input('Qual o número você quer saber o fatorial? '))
fatorial = n
for c in range(n-1, 1, -1):
    fatorial = fatorial * c
print('O fatorial de {} é igual a {}'.format(n, fatorial))