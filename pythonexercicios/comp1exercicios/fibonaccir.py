# Ewerton Vieira
# 02/05/2019
#
# programa que mostra o enesimo termo da sequencia de Fibonacci

def fibonacci(termo):
	a, b = 1, 1
	if termo > 2:
		a, b = fibonacci(termo - 1)
	return b, a + b

termo = int(input('Entre com um número inteiro: '))
numero = fibonacci(termo)[0]
print(numero)
