# Ewerton Vieira
# 06/06/19
#
# funcoes de arquivo


def main():
	return True

def abrir():
	nome = input('Qual o nome do arquivo? ')
	nome += '.txt'
	try:
		arquivo = open(nome, 'a+')
	except FileNotFoundError:
		arquivo = open(nome, 'w')
	return arquivo

def inserir(arquivo):
	cont = 1
	res = 'SIM'
	while cont <= 50 and res in 'SIM':
		nome = input('Digite o {}° nome: '.format(cont))
		arquivo.write(nome+'\n')
		cont += 1
		res = input('Quer continuar? ').upper()
	arquivo.close()

def imprimir(arquivo):
	arquivo.seek(0)
	print(arquivo.read())
	arquivo.close()

def ordenar(arquivo):
	arquivo.seek(0)

ordenar(abrir())
