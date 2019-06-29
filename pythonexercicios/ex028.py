from random import randint
from time import sleep
print('\033[33m-=-'*20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m-=-\033[m'*20)
n1 = randint(0, 5)
n2 = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...')
sleep(3)
if n1 == n2:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print(f'\033[31mGANHEI! Eu pensei no {n1} e não no {n2}!\033[m')
