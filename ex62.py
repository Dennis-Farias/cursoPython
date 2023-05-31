a1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))
termos = 1
PA = a1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while termos <= total:
        print('{} -'.format(PA), end=' ')
        PA = PA + r
        termos += 1
    print('PAUSA')
    print()
    mais = int(input('Você quer saber mais quantos termos? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
