from datetime import date
maioridade = 0
for c in range(1,8):
    ano = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        maioridade = maioridade + 1
print('Dessas 7 pessoas, {} já atingiram a maioridade e {} ainda não atingiram'.format(maioridade, 7 - maioridade))