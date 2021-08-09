frase = 'Ferramentas de fatiamento de strings'
print('[::]: ', frase[::])
print('[5:]: ', frase[5:])
print('[::2]: ', frase[::2])
print('[5:20]: ', frase[5:20])
print('[5:30:2]', frase[5:30:2])
print('-' * 67)
frase1 = 'Ferramentas de Análise de strings'
print(frase1, '\nA função len(x) diz o número de espaço ocupado pela string')
print('A variável frase tem', len(frase1), 'de espaço')
print('a função frase1.count(x) verifica um determinado número de letras em uma variável. por ex:\n na variável frase1 há {} letras a'.format(frase1.count('a')))
print('a função frase1.find(x) vai te dizer o número da posição inicial da string inserida. ex\nNa variável frase1 a string Análise inicia na posição', frase1.find('Análise'))
print('Esse comando irá responder True or False na verificação da existência de determinada string em uma variável.\n{}'.format('strings' in frase1))
print('-' * 67)
frase2 = 'Comandos de transformação de strings'
print(frase2.replace('Comandos', 'Métodos'))
print(frase2.upper())
print(frase2.lower())
print(frase2.capitalize())
print(frase2.title())
frase3 = '   Métodos de transformação de strings   '
print(frase3.strip())
print(frase3.rstrip())
print(frase3.lstrip())
print('-' * 67)
frase4 = 'Divisão e junção de strings'
print(frase4.split())
frase4a = frase4.split()
print(' '.join(frase4a))