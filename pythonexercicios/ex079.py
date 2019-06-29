l = []
c = 'S'
while c == 'S':
    n = int(input('Digite um valor: ').strip())
    if n not in l:
        l.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        c = input('Quer continuar? [S/N]').strip().upper()[0]
        if c in 'SN':
            break
print('-='*30)
print(f'Você digitou os valores {sorted(l)}')
