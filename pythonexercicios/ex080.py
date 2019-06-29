l = []
for c in range(0, 5):
    n = int(input(f'Digite um valor: ').strip())
    if c == 0 or n >= l[-1]:
        l.append(n)
        print('Adicionado ao final da lista...')
    else:
        p = 0
        while True:
            if n <= l[p]:
                l.insert(p, n)
                print(f'Adicionado na posição {p} da lista...')
                break
            p += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {l}')
