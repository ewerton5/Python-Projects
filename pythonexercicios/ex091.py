from random import randint
from time import sleep
d = {}
l = []
for c in range(1, 5):
    d[f'Jogador {c}'] = randint(1, 6)
print('Valores sorteados:')
for k, v in d.items():
    print(f'    O {k} tirou {v} no dado.')
    sleep(1)
print('Ranking dos jogadores:')
l = sorted(d.items(), key=lambda x: x[1], reverse=True)
for i, c in enumerate(l):
    print(f'    {i+1}° lugar: {c[0]} com {c[1]}')
    sleep(1)
