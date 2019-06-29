# Ewerton Vieira
# aula 18 de abril
#
# programa monstra os numeros impares até N

n = int(input('Entre com um número inteiro: '))
print(1, end='')
for c in range(3, n + 1, 2):
  print(', ', c, end='')