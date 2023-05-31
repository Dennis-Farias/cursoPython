a1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))
termos = 1
PA = a1
while termos <= 10:
    print('{} -'.format(PA), end=' ')
    PA = PA + r
    termos += 1
print('FIM')