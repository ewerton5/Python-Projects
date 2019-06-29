nome = []
idade = []
for c in range(1, 3):
	nome.append(input('Nome do aluno {}: '.format(c)))
	idade.append(input('Idade do aluno {}: '.format(c)))
print('Nome: ', nome[0],'\nIdade: ', idade[0],'\nNome: ', nome[1],'\nIdade: ', idade[1])
print('  Nome  |  Idade  \n{:^8}|{:^8}\n{:^8}|{:^8}'.format(nome[0], idade[0], nome[1], idade[1]))
