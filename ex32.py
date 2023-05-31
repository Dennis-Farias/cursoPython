ano = int(input("Que ano você quer analisar? Digite 0 para analisar o ano atual: "))
from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano \033[34m{}\033[m é bissexto".format(ano))
else:
    print("O ano \033[34m{}\033[m não é bissexto".format(ano))