l = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: ').strip())
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)
print('-='*30)
print(f'Os valores pares digitados foram: {sorted(l[0])}')
print(f'Os valores ímpares digitados foram: {sorted(l[1])}')
