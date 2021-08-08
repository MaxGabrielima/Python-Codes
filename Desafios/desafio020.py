#Neste desafio teremos o mesmo passo a passo do 019, com uma única diferença
import random
a1 = input('Nome do primeiro Aluno : ')
a2 = input('Nome do segundo Aluno : ')
a3 = input('Nome do terceiro Aluno : ')
a4 = input('Nome do quarto Aluno : ')

alunos = [a1, a2, a3, a4]
print(random.sample(alunos, k=4))

#o comando random.sample(alunos) retornará uma versão embaralhada da sua lista; você precisa especificar quantos elementos o programa irá selecionar utilizando k=x, ou apenas x. Você também pode utilizar outro método:
	#random.shuffle(alunos) 
	#atenção: no caso do Shuffle você deve adicionar um print em outra linha para que ele mostre a lista embaralhada, diferente do sample. ex:
		#random.shuffle(alunos)
		#print(alunos)