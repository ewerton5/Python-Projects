from random import randint
from time import sleep
print('\033[33m-=-'*10)
print('\033[36mTic-tac-toe'
      '\n[1] 1 Jogador'
      '\n[2] 2 Jogadores'
      '\n[3] Sair')
f = False
while not f:
    o = int(input('\033[36mSua opção: ').strip())
    if o == 1:
        print('\033[33m-=-'*10)
        print('\033[36mJogue Tic-tac-toe contra mim'
              '\nVou te ensinar a jogar'
              '\nVocê escolhe um número de 1 a 9'
              '\nCada número corresponde a uma'
              '\nposição da seguinte forma'
              '\n\033[4;35m 1 | 2 | 3 '
              '\n 4 | 5 | 6 '
              '\n\033[35m 7 | 8 | 9 \033[m')
        print('\033[33m-=-\033[m'*10)
        p = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        j1g = j2g = False
        while not j1g and not j2g:
            op = False
            while not op:
                j = int(input(f'\033[34mJogador: ').strip())
                if j == 1 and p[1] not in 'XO':
                    p[1] = 'X'
                    op = True
                elif j == 2 and p[2] not in 'XO':
                    p[2] = 'X'
                    op = True
                elif j == 3 and p[3] not in 'XO':
                    p[3] = 'X'
                    op = True
                elif j == 4 and p[4] not in 'XO':
                    p[4] = 'X'
                    op = True
                elif j == 5 and p[5] not in 'XO':
                    p[5] = 'X'
                    op = True
                elif j == 6 and p[6] not in 'XO':
                    p[6] = 'X'
                    op = True
                elif j == 7 and p[7] not in 'XO':
                    p[7] = 'X'
                    op = True
                elif j == 8 and p[8] not in 'XO':
                    p[8] = 'X'
                    op = True
                elif j == 9 and p[9] not in 'XO':
                    p[9] = 'X'
                    op = True
                else:
                    print('Você não pode Jogar aí')
            print('\033[33m-=-\033[m' * 10)
            print(f'\033[4;35m {p[1]} | {p[2]} | {p[3]} '
                  f'\n {p[4]} | {p[5]} | {p[6]} '
                  f'\n\033[35m {p[7]} | {p[8]} | {p[9]} ')
            print('\033[33m-=-\033[m' * 10)
            if p[1] == p[2] == p[3] == 'X':
                print('\033[34mJogador ganhou!')
                j1g = True
            elif p[4] == p[5] == p[6] == 'X':
                print('\033[34mJogador ganhou!')
                j1g = True
            elif p[7] == p[8] == p[9] == 'X':
                print('\033[34mJogador ganhou!')
                j1g = True
            elif p[1] == p[4] == p[7] == 'X':
                print('\033[34mJogador ganhou!')
                j1g = True
            elif p[2] == p[5] == p[8] == 'X':
                print('\033[34mJogador ganhou!')
                j1g = True
            elif p[3] == p[6] == p[9] == 'X':
                print('\033[34mJogador ganhou!')
                j1g = True
            elif p[1] == p[5] == p[9] == 'X':
                print('\033[34mJogador ganhou!')
                j1g = True
            elif p[7] == p[5] == p[3] == 'X':
                print('\033[34mJogador ganhou!')
                j1g = True
            elif p[1] in 'OX' and p[2] in 'OX' and p[3] in 'OX' and p[4]in 'OX' \
                    and p[5] in 'OX' and p[6] in 'OX' and p[7] in 'OX' \
                    and p[8] in 'OX' and p[9] in 'OX' and not j1g and not j2g:
                print('\033[36mDeu velha!')
                j1g = True
            op = False
            while not op and not j1g:
                j = randint(1, 9)
                if j == 1 and p[1] not in 'XO':
                    p[1] = 'O'
                    op = True
                    sleep(0.5)
                    print(f'\033[31mComputador: {j}')
                    sleep(0.5)
                elif j == 2 and p[2] not in 'XO':
                    p[2] = 'O'
                    op = True
                    sleep(0.5)
                    print(f'\033[31mComputador: {j}')
                    sleep(0.5)
                elif j == 3 and p[3] not in 'XO':
                    p[3] = 'O'
                    op = True
                    sleep(0.5)
                    print(f'\033[31mComputador: {j}')
                    sleep(0.5)
                elif j == 4 and p[4] not in 'XO':
                    p[4] = 'O'
                    op = True
                    sleep(0.5)
                    print(f'\033[31mComputador: {j}')
                    sleep(0.5)
                elif j == 5 and p[5] not in 'XO':
                    p[5] = 'O'
                    op = True
                    sleep(0.5)
                    print(f'\033[31mComputador: {j}')
                    sleep(0.5)
                elif j == 6 and p[6] not in 'XO':
                    p[6] = 'O'
                    op = True
                    sleep(0.5)
                    print(f'\033[31mComputador: {j}')
                    sleep(0.5)
                elif j == 7 and p[7] not in 'XO':
                    p[7] = 'O'
                    op = True
                    sleep(0.5)
                    print(f'\033[31mComputador: {j}')
                    sleep(0.5)
                elif j == 8 and p[8] not in 'XO':
                    p[8] = 'O'
                    op = True
                    sleep(0.5)
                    print(f'\033[31mComputador: {j}')
                    sleep(0.5)
                elif j == 9 and p[9] not in 'XO':
                    p[9] = 'O'
                    op = True
                    sleep(0.5)
                    print(f'\033[31mComputador: {j}')
                    sleep(0.5)
            if not j1g and not j2g:
                print('\033[33m-=-\033[m' * 10)
                print(f'\033[4;35m {p[1]} | {p[2]} | {p[3]} '
                      f'\n {p[4]} | {p[5]} | {p[6]} '
                      f'\n\033[35m {p[7]} | {p[8]} | {p[9]} ')
                print('\033[33m-=-\033[m' * 10)
            if p[1] == p[2] == p[3] == 'O':
                print('\033[31mComputador ganhou!')
                j2g = True
            elif p[4] == p[5] == p[6] == 'O':
                print('\033[31mComputador ganhou!')
                j2g = True
            elif p[7] == p[8] == p[9] == 'O':
                print('\033[31mComputador ganhou!')
                j2g = True
            elif p[1] == p[4] == p[7] == 'O':
                print('\033[31mComputador ganhou!')
                j2g = True
            elif p[2] == p[5] == p[8] == 'O':
                print('\033[31mComputador ganhou!')
                j2g = True
            elif p[3] == p[6] == p[9] == 'O':
                print('\033[31mComputador ganhou!')
                j2g = True
            elif p[1] == p[5] == p[9] == 'O':
                print('\033[31mComputador ganhou!')
                j2g = True
            elif p[7] == p[5] == p[3] == 'O':
                print('\033[31mComputador ganhou!')
                j2g = True
            elif p[1] in 'OX' and p[2] in 'OX' and p[3] in 'OX' and p[4]in 'OX' \
                    and p[5] in 'OX' and p[6] in 'OX' and p[7] in 'OX' and p[8] in 'OX' \
                    and p[9] in 'OX' and not j1g and not j2g:
                print('\033[31mDeu velha!')
                j1g = True
            if j1g or j2g:
                print('\033[33m-=-\033[m' * 10)
                while True:
                    jn = input('\033[32mJogar novamente? [S/N] ').strip()[0]
                    if jn in 'Ss':
                        print('\033[33m-=-\033[m' * 10)
                        p = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                        j1g = j2g = False
                        break
                    elif jn in 'Nn':
                        print('\033[33m-=-\033[m' * 10)
                        print('\033[35mVoltanto ao menu inicial...')
                        sleep(1)
                        print('\033[33m-=-' * 10)
                        print('\033[36mTic-tac-toe'
                              '\n[1] 1 Jogador'
                              '\n[2] 2 Jogadores'
                              '\n[3] Sair')
                        break
                    else:
                        print('Opção inválida, tente novamente.')
    if o == 2:
        print('\033[33m-=-'*10)
        print('\033[36mJogue Tic-tac-toe com seu amigo'
              '\nVou te ensinar a jogar'
              '\nVocê escolhe um número de 1 a 9'
              '\nCada número corresponde a uma'
              '\nposição da seguinte forma'
              '\n\033[4;35m 1 | 2 | 3 '
              '\n 4 | 5 | 6 '
              '\n\033[35m 7 | 8 | 9 \033[m')
        print('\033[33m-=-\033[m'*10)
        p = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        j1g = j2g = False
        while not j1g and not j2g:
            op = False
            while not op:
                j = int(input(f'\033[34mJogador 1: ').strip())
                if j == 1 and p[1] not in 'XO':
                    p[1] = 'X'
                    op = True
                elif j == 2 and p[2] not in 'XO':
                    p[2] = 'X'
                    op = True
                elif j == 3 and p[3] not in 'XO':
                    p[3] = 'X'
                    op = True
                elif j == 4 and p[4] not in 'XO':
                    p[4] = 'X'
                    op = True
                elif j == 5 and p[5] not in 'XO':
                    p[5] = 'X'
                    op = True
                elif j == 6 and p[6] not in 'XO':
                    p[6] = 'X'
                    op = True
                elif j == 7 and p[7] not in 'XO':
                    p[7] = 'X'
                    op = True
                elif j == 8 and p[8] not in 'XO':
                    p[8] = 'X'
                    op = True
                elif j == 9 and p[9] not in 'XO':
                    p[9] = 'X'
                    op = True
                else:
                    print('Você não pode Jogar aí')
            print('\033[33m-=-\033[m' * 10)
            print(f'\033[4;35m {p[1]} | {p[2]} | {p[3]} '
                  f'\n {p[4]} | {p[5]} | {p[6]} '
                  f'\n\033[35m {p[7]} | {p[8]} | {p[9]} ')
            print('\033[33m-=-\033[m' * 10)
            if p[1] == p[2] == p[3] == 'X':
                print('\033[34mJogador 1 ganhou!')
                j1g = True
            elif p[4] == p[5] == p[6] == 'X':
                print('\033[34mJogador 1 ganhou!')
                j1g = True
            elif p[7] == p[8] == p[9] == 'X':
                print('\033[34mJogador 1 ganhou!')
                j1g = True
            elif p[1] == p[4] == p[7] == 'X':
                print('\033[34mJogador 1 ganhou!')
                j1g = True
            elif p[2] == p[5] == p[8] == 'X':
                print('\033[34mJogador 1 ganhou!')
                j1g = True
            elif p[3] == p[6] == p[9] == 'X':
                print('\033[34mJogador 1 ganhou!')
                j1g = True
            elif p[1] == p[5] == p[9] == 'X':
                print('\033[34mJogador 1 ganhou!')
                j1g = True
            elif p[7] == p[5] == p[3] == 'X':
                print('\033[34mJogador 1 ganhou!')
                j1g = True
            elif p[1] in 'OX' and p[2] in 'OX' and p[3] in 'OX' and p[4]in 'OX' \
                    and p[5] in 'OX' and p[6] in 'OX' and p[7] in 'OX' and p[8] in 'OX' \
                    and p[9] in 'OX' and not j1g and not j2g:
                print('\033[36mDeu velha!')
                j1g = True
            op = False
            while not op and not j1g:
                j = int(input(f'\033[31mJogador 2: ').strip())
                if j == 1 and p[1] not in 'XO':
                    p[1] = 'O'
                    op = True
                elif j == 2 and p[2] not in 'XO':
                    p[2] = 'O'
                    op = True
                elif j == 3 and p[3] not in 'XO':
                    p[3] = 'O'
                    op = True
                elif j == 4 and p[4] not in 'XO':
                    p[4] = 'O'
                    op = True
                elif j == 5 and p[5] not in 'XO':
                    p[5] = 'O'
                    op = True
                elif j == 6 and p[6] not in 'XO':
                    p[6] = 'O'
                    op = True
                elif j == 7 and p[7] not in 'XO':
                    p[7] = 'O'
                    op = True
                elif j == 8 and p[8] not in 'XO':
                    p[8] = 'O'
                    op = True
                elif j == 9 and p[9] not in 'XO':
                    p[9] = 'O'
                    op = True
                else:
                    print('Você não pode jogar aí')
            if not j1g and not j2g:
                print('\033[33m-=-\033[m' * 10)
                print(f'\033[4;35m {p[1]} | {p[2]} | {p[3]} '
                      f'\n {p[4]} | {p[5]} | {p[6]} '
                      f'\n\033[35m {p[7]} | {p[8]} | {p[9]} ')
                print('\033[33m-=-\033[m' * 10)
            if p[1] == p[2] == p[3] == 'O':
                print('\033[31mJogador 2 ganhou!')
                j2g = True
            elif p[4] == p[5] == p[6] == 'O':
                print('\033[31mJogador 2 ganhou!')
                j2g = True
            elif p[7] == p[8] == p[9] == 'O':
                print('\033[31mJogador 2 ganhou!')
                j2g = True
            elif p[1] == p[4] == p[7] == 'O':
                print('\033[31mJogador 2 ganhou!')
                j2g = True
            elif p[2] == p[5] == p[8] == 'O':
                print('\033[31mJogador 2 ganhou!')
                j2g = True
            elif p[3] == p[6] == p[9] == 'O':
                print('\033[31mJogador 2 ganhou!')
                j2g = True
            elif p[1] == p[5] == p[9] == 'O':
                print('\033[31mJogador 2 ganhou!')
                j2g = True
            elif p[7] == p[5] == p[3] == 'O':
                print('\033[31mJogador 2 ganhou!')
                j2g = True
            elif p[1] in 'OX' and p[2] in 'OX' and p[3] in 'OX' and p[4]in 'OX' \
                    and p[5] in 'OX' and p[6] in 'OX' and p[7] in 'OX' and p[8] in 'OX' \
                    and p[9] in 'OX' and not j1g and not j2g:
                print('\033[31mDeu velha!')
                j1g = True
            if j1g or j2g:
                print('\033[33m-=-\033[m' * 10)
                while True:
                    jn = input('\033[32mJogar novamente? [S/N] ').strip()[0]
                    if jn in 'Ss':
                        print('\033[33m-=-\033[m' * 10)
                        p = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                        j1g = j2g = False
                        break
                    elif jn in 'Nn':
                        print('\033[33m-=-\033[m' * 10)
                        print('\033[35mVoltanto ao menu inicial...')
                        sleep(1)
                        print('\033[33m-=-' * 10)
                        print('\033[36mTic-tac-toe'
                              '\n[1] 1 Jogador'
                              '\n[2] 2 Jogadores'
                              '\n[3] Sair')
                        break
                    else:
                        print('Opção inválida, tente novamente.')
    elif o == 3:
        print('\033[35mFinalizando jogo...')
        sleep(1)
        f = True
    else:
        print('Opção inválida, tente novamente.')
print('\033[33m-=-\033[m' * 10)
print('\033[32mO jogo terminou!')
