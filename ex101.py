def voto(anonasc):
    from datetime import date
    idade = date.today().year - anonasc
    if 65 >= idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else: 
        return f'Com {idade} anos: NÃO VOTA.'


print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
