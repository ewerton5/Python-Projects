# Ewerton Vieira
# aula 18 de abril
#
# programa que faz o fatorial de um numero

from math import factorial
n = int(input('Entre com um número inteiro: '))
print('{}! = {} '.format(n, n), end='')
for c in range(n - 1, 0, -1):
  print('x {} '.format(c), end='')
print('=', factorial(n))