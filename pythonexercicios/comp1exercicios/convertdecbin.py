# Ewerton Vieira
# 02/05/2019
#
# programa que converte decimal em binario

def converter(decimal):
	binario = ''
	if decimal < 2:
		binario = str(decimal)
	else:
		binario += converter(decimal // 2) +  str(decimal % 2)
	return binario

decimal = int(input('Entre com um número inteiro: '))
binario = converter(decimal)
print(binario)
