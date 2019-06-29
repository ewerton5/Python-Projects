# Ewerton Vieira
# aula 18 de abril
#
# programa que escreve todos os numeros primos até um limite qualquer

lim = int(input('Entre com um limite: '))
if lim == 2:
	print('2 é o primeiro número primno.')
else:
	print('Os números primos até {} são 2'.format(lim), end='')
	for numero in range(3, lim + 1):
		cont = 0
		for c in range(1, numero + 1):
			if numero % c == 0:
				cont += 1
		if cont == 2:
			print(',', numero, end='')
