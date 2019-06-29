d = {'nome': [], 'sexo': [], 'idade': []}
while True:
    d['nome'].append(input('Nome: ').strip())
    s = ' '
    while s not in 'MF':
        s = input('Sexo: [M/F] ').upper().strip()[0]
    d['sexo'].append(s)
    d['idade'].append(int(input('Idade: ').strip()))
    r = ' '
    while r not in 'SN':
        r = input('Quer consinuar? [S/N] ').upper().strip()[0]
    if r == 'N':
        break
print('-='*30)
m = sum(d["idade"])/len(d["idade"])
print(f'- O grupo tem {len(d["nome"])} pessoas.'
      f'\n- A média de idade é de {m:5.2f} anos.'
      '\n- As mulheres cadastradas foram:', end=' ')
for i, c in enumerate(d['sexo']):
    if c == 'F':
        print(d['nome'][i], end=' ')
print('\n- Lista das pessoas que estão acima da média:')
for i, c in enumerate(d['idade']):
    if c > m:
        for k, v in d.items():
            print(f'    {k} = {v[i]}', end='; ')
        print()
print('<< ENCERRADO >>')
