print('\033[33m-=-'*21)
print('-=-'*7+'\033[34m Calculador  de  PA  '+'\033[33m-=-\033[m'*7)
print('\033[33m-=-\033[m'*21)
p = int(input('Primeiro termo: ').strip())
r = int(input('Razão: ').strip())
n = 0
u = 10
while u != 0:
    if u < 0:
        print('Opção inválida, tente novamente.')
    else:
        while u > 0:
            print(p, end=' → ')
            p += r
            n += 1
            u -= 1
        print('PAUSA')
    u = int(input('Quantos termos a mais você quer ver? ').strip())
print(f'Progressão finalizada com {n} termos mostrados.')
