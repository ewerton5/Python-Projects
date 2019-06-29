ch = cm = cp = 0
while True:
    print(f'----- CADASTRE UMA PESSOA -----')
    i = int(input('Idade: '))
    s = input('Sexo [M/F]: ').strip()
    while s not in 'MmFf':
        print('Opção inválida, tente novamente.')
        s = input('Sexo [M/F]:').strip()
    if i >= 18:
        cp += 1
    if s in 'Mm':
            ch += 1
    elif s in 'Ff' and i < 20:
            cm += 1
    while True:
        o = input('Quer continuar? ').strip().upper()
        if o in 'SIMNÂO':
            break
        else:
            print('Opção inválida, tente novamente.')
    if o not in 'SIM':
        break
print(f'====== FIM DO PROGRAMA ======'
      f'\nTotal de pessoas com mais de 18 anos: {cp}'
      f'\nAo todo temos {ch} homens cadastrados.'
      f'\nE temos {cm} mulheres com menos de 20 anos.')
