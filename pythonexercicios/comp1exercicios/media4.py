numero = []
soma = 0
for c in range(1, 5):
	numero.append(int(input('Digite o {}° número inteiro: '.format(c))))
media = (numero[0] + numero[1] + numero[2] + numero[3])/4
print('A média vale: ', media)
