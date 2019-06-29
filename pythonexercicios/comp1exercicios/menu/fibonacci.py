# Ewerton Vieira
# 25/04/2019
#
# Programa que mostra o enésimo número da sequencia de fibonacci

def fibonacci(numero):
	a, b = 1, 1
	for c in range(0, numero - 1):
		a, b = b, a + b
	return a

numero = int(input('Digite um número inteiro: '))

print('O {}° número da sequência de Fibonacci é {}'.format(numero, fibonacci(numero)))
