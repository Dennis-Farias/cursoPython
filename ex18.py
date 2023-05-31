from math import cos
from math import tan
from math import sin
from math import radians
ang = float(input("Digite um ângulo: "))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print("Informações sobre esse ângulo, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}".format(seno, cosseno, tangente))