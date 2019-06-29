lista = [[], [], []]
p = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l].append(int(input(f'Digite um valor para [{l}, {c}]: ').strip()))
        if lista[l][c] % 2 == 0:
            p += lista[l][c]
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {p}.'
      f'\nA soma dos valores da terceira coluna é {lista[0][2]+lista[1][2]+lista[2][2]}.'
      f'\nO maior valor da segunda linha é {max(lista[1])}.')
