n = int(input('Digite um número para ver o seu fatorial: ').strip())
if n == 0:
    print('0! = 1')
elif n < 0:
    print('Não existe fatorial de número negativo.')
else:
    f = 1
    print(f'{n}! =', end='')
    while n != 1:
        print(f' {n} ', end='x')
        f *= n
        n -= 1
    print(f' 1 = {f}')
