lista = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        lista[l].append(int(input(f'Digite um valor para [{l}, {c}]: ').strip()))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()
