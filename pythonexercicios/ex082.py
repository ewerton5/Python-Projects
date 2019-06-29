l = []
p = []
i = []
c = 'S'
while c == 'S':
    l.append(int(input('Digite um valor: ').strip()))
    while True:
        c = input('Quer continuar? [S/N]').strip().upper()[0]
        if c in 'SN':
            break
for c in l:
    if c % 2 == 0:
        p.append(c)
    else:
        i.append(c)
print('-='*30)
print(f'A lista completa é {l}')
print(f'A lista de pares é {p}')
print(f'A lista de ímpares é {i}')
