# Ewerton Vieira
# 25/04/2019
#
# Programa que conta o número de caracteres numa frase

def contar(frase, caracter):
	cont = 0
	for c in range(0, len(frase)):
		if frase[c] == caracter:
			cont += 1 
	return cont

frase = input('Digite uma frase: ').lower()
caracter = input('Digite um caracter contido na frase: ').lower()

print('O caracter `{}` aparece {} vezes na frase'.format(caracter, contar(frase, caracter)))
