import math
from math import sqrt

c1 = float(input('Digite o valor do primeiro cateto: '))
c2 = float(input('Digite o valor do segundo cateto: '))
q = (c1 ** 2) + (c2 ** 2) 
h = math.sqrt (q)
print('Um triângulo retângulo com catetos de valores {} e {}, terá uma hipotenusa com o valor {}!'.format(c1, c2, h))
