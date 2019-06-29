# Ewerton Vieira
# 02/05/2019
#
# programa que calcula o protudo entre dois numeros

def multiplicar(fator1, fator2):
	multiplicador = fator1
	if fator2 == 0:
		multiplicador = 0
	elif fator2 > 0:
		multiplicador += multiplicar(fator1, fator2 - 1)
	return multiplicador

fator1 = int(input('Entre com um número inteiro: '))
fator2 = int(input('Entre com outro número inteiro: '))
print(multiplicar(fator1, fator2))
