l = []
d = {'nome': input('Nome do Jogador: ').strip()}
j = int(input(f'Quantas partidas {d["nome"]} jogou? ').strip())
for c in range(0, j):
    l.append(int(input(f'Quantos gols na partida {c}? ').strip()))
d['gols'] = l[:]
d['total'] = sum(l)
print('-='*30)
print(d)
print('-='*30)
for k, v in d.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {d["nome"]} jogou {j} partidas.')
for i, c in enumerate(d['gols']):
    print(f'    => Na pardida {i}, fez {c} gols.')
print(f'Foi um total de {d["total"]} gols.')
