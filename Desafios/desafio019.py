#vamos importar o módulo random, que gera números ou elementos de uma lista de forma pseudoaleatória.
import random
a1 = input('Nome do primeiro Aluno : ')
a2 = input('Nome do segundo Aluno : ')
a3 = input('Nome do terceiro Aluno : ')
a4 = input('Nome do quarto Aluno : ')
#aqui criamos variáveis
alunos = [a1, a2, a3, a4]
#em seguida adicionamos à uma lista
print(random.choice(alunos))
#E printamos com random.choice para que o programa escolha um dos alunos. 
#essa é apenas uma das milhares de forma de resolver.