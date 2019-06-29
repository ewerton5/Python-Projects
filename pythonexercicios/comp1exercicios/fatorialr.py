# Ewerton Vieira
# 02/05/2019
#
# programa que calcula o fatorial de um numero

def fatorial(numero):
	if numero > 1:
		numero *=fatorial(numero-1)
	return numero

numero = int(input('Entre com um número inteiro: '))
print(fatorial(numero))
