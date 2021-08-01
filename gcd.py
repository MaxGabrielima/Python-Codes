import math
from math import gcd
print('_' * 67)
print('Digite dois números para ver o maior divisor comum entre eles')

n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
m = math.gcd (n1, n2)
print('O maior divisor comum entre {} e {} é {}'.format(n1, n2, m))
print('_' * 67)

