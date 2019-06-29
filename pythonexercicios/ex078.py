l = []
for c in range(0, 5):
    l.append(int(input(f'Digite um valor para a Posição {c}: ').strip()))
print(f'Você digitou os valores {l}')
print(f'O maior valor digitado foi {max(l)} nas posições', end=' ')
for c, v in enumerate(l):
    if max(l) == v:
        print(f'{c}...', end=' ')
print(f'\nO menor valor digitado foi {min(l)} nas posições', end=' ')
for c, v in enumerate(l):
    if min(l) == v:
        print(f'{c}...', end=' ')
