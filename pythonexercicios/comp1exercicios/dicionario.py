# Ewerton
# 05/30
#
# Funções dos dicionarios

def main():
	lista1 = []
	lista2 = []
	menu()
	opcao = int(input('Sua opção: '))
	while opcao != 6:
		if opcao == 1:
			nome = input('Digite o nome: ')
			idade = int(input('Digite a idade: '))
			notas = []
			nota = 0
			while nota >= 0: 
				nota = int(input('Digite a nota(negativo para): '))
				notas.append(nota)
			cadastrar(nome, idade, notas)
		elif opcao == 2:
			num = int(input('Qual lista deseja imprimir? '))
			if num == 1:
				imprimir(lista1)
			if num == 2:
				imprimir(lista2)
		opcao = int(input('Sua opção: '))

def menu():
	print('''Selecione uma opção:
	[1] Cadastrar aluno
	[2] Imprimir lista de alunos
	[3] Mostrar informação de um aluno
	[4] Ordenar lista
	[5] Acrescentar aluno
	[6] Sair''')

def cadastrar(nome, idade, notas):
	soma = 0
	for c in notas:
		soma += c
	media = soma/len(notas)
	dicionario = {'Nome': nome, 'Idade': idade, 'Notas': notas, 'Média': media}
	return dicionario

def imprimir(lista):
	for c in range(len(lista)):
		print('{:10}{:10}{:10}{:10}'.format(lista[c]['Nome'], lista[c]['Idade'], lista[c]['Notas'], lista[c]['Média']))

def imprimirAluno(c):
	print('{:10}{:10}{:10}{:10}'.format(lista[c]['Nome'], lista[c]['Idade'], lista[c]['Notas'], lista[c]['Média']))

def ordenar(lista):
	return lista.sort()

def acrescentarOrdenado(lista, nome, idade, notas):
	dicionario = cadastrar(nome, idade, notas)
	return ordenar(lista.append(dicionario))
	
main()
