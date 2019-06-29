s = float(input('Qual o salário do funcionário? R$'))
if s > 1250:
    ns = s*1.1
else:
    ns = s*1.15
print(f'Quem ganhava R${s:.2f} passa a ganhar R${ns:.2f} agora.')
