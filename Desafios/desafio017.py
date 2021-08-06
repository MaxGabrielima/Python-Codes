import math 
from math import sqrt 

print(67 * "_")
co = float(input('Digite o valor do cateto oposto: '))
print(67 * "_")
ca = float(input('Digite o valor do cateto adjascente: '))
print(67 * "_")
h = sqrt(co * co + ca * ca)
print('A hipotenusa é igual à {:.2f}'.format(h))