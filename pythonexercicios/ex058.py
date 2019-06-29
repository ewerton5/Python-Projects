from random import randint
print('\033[33m-=-'*20)
print('\033[34mVou pensar em um número entre 0 e 10. Tente adivinhar...')
print('\033[33m-=-\033[m'*20)
n1 = randint(0, 10)
n2 = int(input('Em que número eu pensei? '))
c = 0
while n1 != n2:
    if n2 > n1:
        print('\033[31mMenos! Tente novamente.\033[m')
    else:
        print('\033[31mMais! Tente novamente.\033[m')
    n2 = int(input('Em que número eu pensei? '))
    c += 1
print(f'\033[32mPARABÉNS! Você conseguiu acertar em {c+1} tentativas!\033[m')
