l = []
c = 'S'
while c == 'S':
    l.append(int(input('Digite um valor: ').strip()))
    while True:
        c = input('Quer continuar? [S/N]').strip().upper()[0]
        if c in 'SN':
            break
print('-='*30)
print(f'Você digitou {len(l)} elementos.')
l.sort(reverse=True)
print(f'Os valores em ordem decrescente são {l}')
if 5 in l:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
