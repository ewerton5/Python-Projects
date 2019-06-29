# Ewerton Vieira
# aula 18 de abril
#
# programa que faz a média de n valores

n=[]
while True:
  aux = int(input('Entre com um número positivo(negativo para finalizar): '))
  if aux >= 0:
    n.append(aux)
  else:
    break
soma = 0
for c in n:
  soma += c
print('A média dos números digitados é', soma/len(n))