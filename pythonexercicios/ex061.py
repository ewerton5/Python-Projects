print('\033[33m-=-'*21)
print('-=-'*7+'\033[34m Calculador  de  PA  '+'\033[33m-=-\033[m'*7)
print('\033[33m-=-\033[m'*21)
p = int(input('Primeiro termo: ').strip())
r = int(input('Razão: ').strip())
n = 1
while n != 11:
    print(p, end=' → ')
    p += r
    n += 1
print('ACABOU')
