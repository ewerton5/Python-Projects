l = [0, 0, 0, 0, 0]
for c in range(0, 5):
    l[c] = float(input(f'Peso da {c+1}° pessoa: '))
print(f'O maior peso é {max(l[0], l[1], l[2], l[3], l[4])}Kg'
      f'\nO menor peso é {min(l[0], l[1], l[2], l[3], l[4])}Kg')
