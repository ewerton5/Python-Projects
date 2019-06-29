# Ewerton Vieira
# 25/04/2019
#
# Programa que faz uma combinação entre dois números

def fatorial(n):
	fat = 1
	for c in range(n, 1, -1):
		fat *= c
	return fat

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite número inteiro menor que o primeiro: '))
print('O combinação entre {} e {} é {}'.format(n1, n2, fatorial(n1)/(fatorial(n2)*fatorial(n1 - n2))))
