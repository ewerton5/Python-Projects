from random import choice
from time import sleep
print('\033[33m-=-'*21)
print('-=-'*7+'\033[34m Vamos jogar Jokenpô '+'\033[33m-=-\033[m'*7)
print('\033[33m-=-\033[m'*21)
pe = 'pedra'
pa = 'papel'
te = 'tesoura'
n1 = choice([pe, pa, te])
n2 = input('\033[36mpedra, papel ou tesoura? ').lower().strip()
if n2 in [pe, pa, te]:
    print('\033[33m-=-'*21)
    print('-=-'*7+f'\033[34m  Eu joguei {n1:^8} '+'\033[33m-=-'*7)
    print('-=-'*7+f'\033[34m  Você jogou {n2:^7} '+'\033[33m-=-'*7)
    print('\033[33m-=-\033[m'*21)
if n2 == pe:
    print('\033[35mHUM, DEIXA EU VER...')
    sleep(1)
    if n1 == pa:
        print(f'\033[31mGANHEI! Eu joguei {pa} e você jogou {pe}!\033[m')
    elif n1 == te:
        print(f'\033[32mPARABÉNS! Você jogou {pe} e eu joguei {te}!\033[m')
    else:
        print(f'\033[34mEMPATE! Nós dois jogamos {pe}!\033[m')
elif n2 == pa:
    print('\033[36mHUM, DEIXA EU VER...')
    sleep(1)
    if n1 == te:
        print(f'\033[31mGANHEI! Eu joguei {te} e você jogou {pa}!\033[m')
    elif n1 == pe:
        print(f'\033[32mPARABÉNS! Você jogou {pa} e eu joguei {pe}!\033[m')
    else:
        print(f'\033[36mEMPATE! Nós dois jogamos {pa}!\033[m')
elif n2 == te:
    print('\033[35mHUM, DEIXA EU VER...')
    sleep(1)
    if n1 == pe:
        print(f'\033[31mGANHEI! Eu joguei {pe} e você jogou {te}!\033[m')
    elif n1 == pa:
        print(f'\033[32mPARABÉNS! Você jogou {te} e eu joguei {pa}!\033[m')
    else:
        print(f'\033[36mEMPATE! Nós dois jogamos {te}!\033[m')
else:
    print('\033[35mNão seja bôbo! você tem que escolher pedra, papel ou tesoura.')
