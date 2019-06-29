# Ewerton Vieira
# 25/04/2019
#
# Programa que mostra um menu de itens

# funcao - fatorial
def fatorial(n):
	fat = 1
	for c in range(n, 1, -1):
		fat *= c
	return fat

# funcao - contar
def contar(frase, caracter):
	cont = 0
	for c in range(0, len(frase)):
		if frase[c] == caracter:
			cont += 1 
	return cont

#funcao - fibonacci
def fibonacci(numero):
	a, b = 1, 1
	for c in range(0, numero - 1):
		a, b = b, a + b
	return a

o = 0
while o != 5:
	print('Menu:\n	[1] Fatorial\n	[2] Combinação\n	[3] Contar\n	[4] Fibonacci\n	[5] Sair')
	o = int(input('Sua opção: '))
	if o == 1:
		 n = int(input('Digite um número inteiro: '))
		 print('O fatorial de {} é {}'.format(n, fatorial(n)))
	elif o == 2:
		n1 = int(input('Digite um número inteiro: '))
		n2 = int(input('Digite número inteiro menor que o primeiro: '))
		print('O combinação entre {} e {} é {}'.format(n1, n2, fatorial(n1)/(fatorial(n2)*fatorial(n1 - n2))))
	elif o == 3:
		frase = input('Digite uma frase: ').lower()
		caracter = input('Digite um caracter contido na frase: ').lower()
		print('O caracter `{}` aparece {} vezes na frase'.format(caracter, contar(frase, caracter)))
	elif o == 4:
		numero = int(input('Digite um número inteiro: '))
		print('O {}° número da sequência de Fibonacci é {}'.format(numero, fibonacci(numero)))
	elif o != 5:
		o = int(input('Opção inválida, tente novamente: '))
print('O progrma terminou. ')