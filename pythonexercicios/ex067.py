while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x  {c:2} = {n*c}')
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
