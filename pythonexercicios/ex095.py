l = []
d = {'nome': [], 'gols': [], 'total': []}
while True:
    print('-'*30)
    n = input('Nome do Jogador: ').strip()
    d['nome'].append(n)
    j = int(input(f'Quantas partidas {n} jogou? ').strip())
    for c in range(0, j):
        l.append(int(input(f'Quantos gols na partida {c}? ').strip()))
    d['gols'].append(l[:])
    d['total'].append(sum(l))
    l.clear()
    r = ' '
    while r not in 'SN':
        r = input('Quer consinuar? [S/N] ').upper().strip()[0]
    if r == 'N':
        break
print('-='*30)
print(f'{"cod"} {"nome":<15}{"gols":<15}total')
print('-'*40)
for c in range(0, len(d['nome'])):
    print(f'{c:>3} {d["nome"][c]:<15}'+str(d['gols'][c])+' '*(15 - len(d['gols'][c])*3)+str(d['total'][c]))
while True:
    print('-' * 40)
    a = int(input('Mostrar dados de qual jogador? (999 interrompe): ').strip())
    if a == 999:
        break
    if a < len(d['gols']):
        print(f'-- LEVANTAMENTO DO JOGADOR {d["nome"][a]}:')
        for i, c in enumerate(d['gols'][a]):
            print(f'    No jogo {i} fez {c} gols.')
    else:
        print(f'ERRO! Não existe jogador com còdigo {a}! Tente novamente')
print('<< VOLTE SEMPRE >>')
