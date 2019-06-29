s = am = 0
print(f'----- CADASTRE OS PRODUTOS -----')
while True:
    n = input('Nome: ').strip()
    p = float(input('Preço: R$'))
    if p > 1000:
        am += 1
    if s == 0 or p < mb:
        mb = p
        nmb = n
    s += p
    while True:
        o = input('Quer continuar? ').strip().upper()
        if o in 'SIMNÂO':
            break
        else:
            print('Opção inválida, tente novamente.')
    if o not in 'SIM':
        break
print(f'====== FIM DO PROGRAMA ======'
      f'\nO total da compra foi R${s:.2f}'
      f'\nTemos {am} produtos custando mais de R$1000.00.'
      f'\nO produto mais barato foi {nmb} que custa R${mb:.2f}.')
