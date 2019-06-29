from random import randint
c = 0
print('\033[33m-=-'*21)
print('-=-'*6+'\033[34m Vamos jogar par ou ímpar  '+'\033[33m-=-\033[m'*6)
print('\033[33m-=-\033[m'*21)
while True:
    nj = int(input('Diga um valor: ').strip())
    pj = ' '
    while True:
        pj = input('Par ou Ímpar? ').strip().lower()
        if pj == 'par' or pj == 'ímpar':
            break
    nc = randint(0,10)
    t = nj + nc
    if t % 2 == 0:
        p = 'par'
    else:
        p = 'ímpar'
    print('\033[33m-=-\033[m'*21)
    print(f'Você jogou {nj} e o computador {nc}. Total de {t} deu {p}.')
    print('\033[33m-=-\033[m'*21)
    if pj == p:
        print('Você venceu!')
        c += 1
        print('Vamos jogar novamente...')
        print('\033[33m-=-\033[m' * 21)
    else:
        print('Você perdeu!')
        print('\033[33m-=-\033[m' * 21)
        break
print(f'GAME OVER! Você venceu {c} vezes.')
