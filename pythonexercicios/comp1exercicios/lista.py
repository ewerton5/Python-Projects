# Ewerton Vieira
# aula 11 de abril
#
# programa das listas

def listazero():
	lista = []
	for c in range(9):
		lista += [0]
	return lista

def imprimir(lista):
	for elem in lista:
		print(elem)

def listaint():
	lista = []
	aux = int(input('Entre com um valor(negativo para): '))
	while aux >= 0:
		lista += [aux]
		aux = int(input('Entre com um valor(negativo para): '))
	return lista

def inverter(lista):
	listainvert = []
	for c in range(len(lista) - 1, -1, -1):
		listainvert += [lista[c]]
	return listainvert

def primos(limite):
	primos = [2]
	for num in range(3, limite + 1):
		i = 0
		while (primos[i] <= num**(0.5) and num % primos[i] != 0):
			i += 1
		if primos[i] > num**(0.5):
			primos += [num]
	return primos

imprimir(primos(331))