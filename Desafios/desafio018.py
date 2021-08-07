#importe os comandos que você usará (ou o módulo todo, com ''import math'', vc decide).
from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
#radians converte o número de graus para radianos.
print('O seno é igual a {:.2f}! \nO cosseno é igual a {:.2f}! \nA tangente é igual a {:.2f}!'.format(sen, cos, tan))
# {:.2f} Para diminuir o número de casas decimais do número. 