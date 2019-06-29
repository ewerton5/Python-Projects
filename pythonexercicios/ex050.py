s1 = 0
s2 = 0
for c in range(0, 6):
    n = int(input(f'Digite o {c + 1}° valor: ').strip())
    if n % 2 == 0:
        s1 += 1
        s2 += n
print(f'Você informou {s1} números pares e a soma foi {s2}')
