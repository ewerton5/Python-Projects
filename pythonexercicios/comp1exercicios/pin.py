# Ewerton Vieira
# aula 18 de abril
#
# jogo do PIN

n = int(input('Entre com um número inteiro: '))
print(1, end='')
for c in range(2, n + 1):
  if c % 4 == 0 and c % 3 != 0:
    print(', PIN', end='')
  else:
    print(', ', c, end='')