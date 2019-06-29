print('\033[33m-=-'*21)
print('-=-'*7+'\033[34m Calculador  de  PA  '+'\033[33m-=-\033[m'*7)
print('\033[33m-=-\033[m'*21)
p = int(input('Primeiro termo: ').strip())
r = int(input('Razão: ').strip())
for c in range(p, p+r*9+1, r):
    print(c, end=' → ')
print('ACABOU')
