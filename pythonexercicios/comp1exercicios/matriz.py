# Ewerton
# 05/23
#
# Funções das matrizes

def zero(n):
	lista = []
	for cont in range(n):
		lista += [0]
	matriz = []
	for cont in range(n):
		matriz += [lista + []]
	return matriz

def imprimir(matriz):
	for linha in range(len(matriz[0])):
		for coluna in range(len(matriz[0])):
			print('{:3}'.format(matriz[linha][coluna]), end='')
		print()

def identidade(n):
	matriz = zero(n) 
	for i in range(len(matriz[0])):
		matriz[i][i] = 1
	return matriz

def permutar(matriz, linha1, linha2):
	matriz[linha1-1], matriz[linha2-1] = matriz[linha2-1], matriz[linha1-1]
	return matriz

def matrizEspecial(n):
	matriz = zero(n)
	for cont in range(n, -2, -1): 
		for linha in range(n):
			for coluna in range(n):
				if linha == cont or coluna == cont:
					matriz[linha][coluna] = cont + 1
		
	return matriz

def multiplicar(matriz1, matriz2):
	matriz = zero(len(matriz1))
	for linha in range(len(matriz1)):
		for coluna in range(len(matriz1)):
			for i in range(len(matriz1)):
		 		matriz[linha][coluna] += matriz1[linha][i]*matriz2[i][coluna]
	return matriz
