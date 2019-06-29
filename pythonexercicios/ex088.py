from random import randint
from time import sleep
j = []
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=-=-=  SORTEANDO 4 JOGOS  -=-=-=')
for u in range(1, n+1):
    j.clear()
    n = randint(1, 60)
    for c in range(0, 6):
        while n in j:
            n = randint(1, 60)
        j.append(n)
    j.sort()
    print(f'Jogo {u}: {j}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
