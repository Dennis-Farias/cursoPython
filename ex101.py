from datetime import date
def voto(anonasc):
    idade = date.today().year - anonasc
    if idade >= 18 or idade < 65:
        return 'VOTO OBRIGATÓRIO'
    elif idade >= 65:
        return 'VOTO OPCIONAL'
    elif idade < 18 and idade >= 16:
        return 'VOTO OPCIONAL'
    else: 
        return 'NÃO VOTA'

print('-' * 30)
anonasc = int(input('Em que ano você nasceu? '))
print(voto(anonasc))
