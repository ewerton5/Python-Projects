# Ewerton Vieira
# aula 11 de abril
#
# programa demonstra se o aluno passara de ano ou nao

nota = []
for c in range(1, 4):
	nota.append(float(input('Digite a nota da {}ª prova: '.format(c))))
faltas = int(input('Digite o número de faltas: '))
aulas = int(input('Digite o número de aulas: '))
media = (nota[0] + nota[1] + nota[2])/3
if media >= 7:
	print('APROVADO')
elif media >= 3:
	if (aulas - faltas)*100/aulas >= 75:
		print('PROVA FINAL')
	else:
		print('REPROVADO POR FALTA')
else:
	print('REPROVADO POR MÉDIA')
