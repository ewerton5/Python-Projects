# Ewerton Vieira
# aula 18 de abril
#
# programa que multiplica usando a soma

n1 = int(input('Entre com um número inteiro: '))
n2 = int(input('Entre com outro número inteiro: '))
while n2 < 0:
  n2 = int(input('Valor invalido, por favor, entre com um número positivo: '))
produto = n1
c = 1
while c <  n2:
  produto += n1
  c += 1
print('O produto entre {} e {} vale {}'.format(n1, n2, produto))