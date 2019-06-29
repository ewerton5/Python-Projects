# Ewerton Vieira
# aula 11 de abril
#
# programa monstra se está frio ou calor

temp = float(input('Digite a temperarura em Celcius '))
if temp > 35:
	print('Está muito calor')
elif temp > 28:
	print('Está calor')
elif temp > 20:
	print('Está agradável')
elif temp > 10:
	print('Está frio')
elif temp > -273:
	print('Está muito frio')
else:
	print('Deixa de ser retardado, essa temperatura não existe!')
