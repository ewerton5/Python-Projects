l = []
r = 'S'
while r == 'S':
    n = input('Nome: ').strip()
    n1 = float(input('Nota 1: ').strip())
    n2 = float(input('Nota 2: ').strip())
    l.append([n, [n1, n2], (n1+n2)/2])
    while True:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
        if r in 'SN':
            break
print('-='*30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, c in enumerate(l):
    print(f'{i:<4}{c[0]:<10}{c[2]:>8.1f}')
while True:
    print('-' * 35)
    a = int(input('Mostrar notas de qual aluno? (999 interrompe): ').strip())
    if a == 999:
        print('FINALIZANDO...')
        break
    if a < len(l):
        print(f'Notas de {l[a][0]} são {l[a][1]}')
print('<<< VOLTE SEMPRE >>>')
