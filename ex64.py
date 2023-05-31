n = 0
termos = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: [999 para parar]'))
    if n != 999:
        termos += 1
        soma += n
print('Você digitou {} números e a soma entre eles é igual a {}'.format(termos, soma))

