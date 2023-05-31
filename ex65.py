pergunta = 'S'
termos = soma = maior = menor = 0
while pergunta == 'S':
    n = int(input('Digite um valor: '))
    pergunta = str(input('Você quer continuar digitando valores? [S/N] ')).upper().strip()[0]
    termos += 1
    soma += n
    if termos == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('A média dos valores digitados é igual a {:.2f}'.format(soma/termos))
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
