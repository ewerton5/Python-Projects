n = int(input('Digite um número inteiro: ').strip())
s = 0
for c in range(1, n+1):
    if n % c == 0:
        s += 1
        print(f'\033[33m{c}', end=' ')
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {s} vezes')
if s == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
