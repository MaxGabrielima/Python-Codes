L = float(input('Largura em Metros: '))
A = float(input('Altura em Metros: '))
R = float(input('Rendimento Fabricante: '))
D = int(input('Demãos: '))
a = L * A
Q = a * D / R
print('A área é de {} metros quadrados e será(ão) necessário(s) {} demão(s), então você precisará de {} litros de tinta'.format(a, D, Q))
