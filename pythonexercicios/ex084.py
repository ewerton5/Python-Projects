p = []
d = []
r = 'S'
while r == 'S':
    d.append(input('Nome: ').strip())
    d.append(int(input('Peso: ').strip()))
    if not p:
        ma = me = d[1]
    elif d[1] > ma:
        ma = d[1]
    elif d[1] < me:
        me = d[1]
    p.append(d[:])
    d.clear()
    while True:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
        if r in 'SN':
            break
ap = []
ep = []
for c in p:
    if c[1] == ma:
        ap.append(c[0])
    if c[1] == me:
        ep.append(c[0])
print('-='*30)
print(f'Ao todo, você cadastrou {len(p)} pessoas.'
      f'\nO maior peso foi de {ma:.1f}Kg. Peso de {ap}'
      f'\nO memor peso foi de {me:.1f}Kg. Peso de {ep}')
