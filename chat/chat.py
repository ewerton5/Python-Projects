from random import randint
from time import localtime
print('Bem Vindo ao chat!')
nome = input('Digite seu nome: ')
cor = '\033[3' + str(randint(1,7)) + 'm'
data = lambda: ' ({C:0>2}/{B:0>2}/{A} {D:0>2}:{E:0>2}:{F:0>2})'.format(**dict(zip([chr(65+i) for i in range(6)], localtime()[:6])))

while True:
  e = input(cor + nome + ': ')
  print('\033[m', end='')
  if e == ':q!':
    break
  if e != '':
    m = open('mensagem.txt', 'a')
    m.write('\n' + cor + nome + data() + ': ' + e + '\033[m')
    m.close()
  m = open('mensagem.txt', 'r')
  print(m.read())
  m.close()
