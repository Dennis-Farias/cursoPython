a1 = int(input('Qual o primeiro termo da P.A? '))
r = int(input('Qual a razão da P.A? '))
a10 = a1 + (10-1) * r
for c in range(a1, a10 + r, r):
    print(c, end=' ')


