tm = 0
it = 0
im = 0
mv = ''
for c in range(1, 5):
    print(f'----- {c}° PESSOA -----')
    n = input('Nome: ').strip()
    i = int(input('Idade: '))
    s = input('Sexo [M/F]:').strip()
    while s not in 'MmFf':
        print('Opção inválida, tente novamente.')
        s = input('Sexo [M/F]:').strip()
    it += i
    if s in 'Mm' and i > im:
            im = i
            mv = n
    elif s in 'Ff' and i < 20:
            tm += 1
print(f'A média de idade do grupo é de {it/4:.2f} anos.'
      f'\nO homem mais velho tem {im} anos e se chama {mv}.'
      f'\nAo todo são {tm} mulheres com menos de 20 anos.')
