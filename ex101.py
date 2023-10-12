from datetime import date
def voto(anonasc):
    
    idade = date.today().year - anonasc
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade < 18 and idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else: 
        return f'Com {idade} anos: NÃO VOTA.'


print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
